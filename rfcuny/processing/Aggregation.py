import pandas as pd
import numpy as np

# Match the RES matrix aggregation based on CenDTect 
# Assign numerical response classes (0-3) in which groups by domain, country, IP Org, and time 
# Computes a T-dimensional vector 
# DataAggregator needed for decision tree implementation utilizing the vectors 

class DataAggregator:
    def __init__(self, anomalyLogger):
        self.anomalyLogger = anomalyLogger
        self.anomalyCount = 0

    def preprocessData(self, cleanedData):
        # Convert to panda dataframe for later processing 
        df = pd.DataFrame(cleanedData) 

        #print(f"[Debug] Cleaned data sample: {df[['matches_template', 'stateful_block', 'controls_failed', 'no_response_in_measurement_matches_template']].head().to_dict()}")
        # Todo: implement t1 to tm (time n to time m)

        # Rename metadata fields to match research paper schema
        df['country'] = df['server_country']
        df['IP Org'] = df['server_organization']
        df['AS'] = df['server_asn'].astype(str)


        # Assign numerical response classes based on metadata fields presented in the dataset 
        # 0 - Benign : Matches template and not stateful_block
        # 1 - Very Unlikely Censorship : Controls failed or no response matching template without stateful_block
        # 2 - Unlikely Censorship : No match but not a clear block, controls_failed or not row['no_response_in_measurement_matches_template'] 
        # 3 - Likely Censorship : stateful_block (true)
        df['response'] = df.apply(
            lambda row: 0 if row['matches_template'] and not row['stateful_block'] else  
                        1 if row['controls_failed'] or (not row['no_response_in_measurement_matches_template'] and not row['stateful_block']) else  
                        2 if row['no_response_in_measurement_matches_template'] and not row['stateful_block'] else  
                        3,
            axis=1
        )

        # Convert to numeric, coerce invalid to NaN
        df['response'] = pd.to_numeric(df['response'], errors='coerce')

        # Identify rows in df with invalid 'response' values anything that is not the numerical class labeling , we log these rows as anomalies,  filter to with valid response values
        invalidResponses = df[~df['response'].isin([0, 1, 2, 3])]
        for _, row in invalidResponses.iterrows():
            self.anomalyLogger.log(row.to_dict(), f"Invalid response: {row['response']}")
            self.anomalyCount += 1
        
        # Get only valid data frames 
        df = df[df['response'].isin([0, 1, 2, 3])]

        # Group by domain and IP Org, aggregate t_vector by start_time
        grouped = df.groupby(['domain', 'IP Org', 'start_time'])

        # Represents the weighted distribution of the four response classes
        def ComputeTVector(group):
            counts = np.bincount(group['response'], minlength=4) 
            total = len(group)
            return counts / total if total > 0 else np.zeros(4)

        # Compute weight per group
        aggregatedWeights = grouped.apply(ComputeTVector).reset_index(name='t_vector')

        # Merge with original data to retain date
        tempDf = df[['domain', 'IP Org', 'start_time', 'date']].drop_duplicates()

        # https://pandas.pydata.org/docs/reference/api/pandas.merge.html
        aggregated = tempDf.merge(aggregatedWeights, on=['domain', 'IP Org', 'start_time'], how='left')

        # Pivot to match matrix structure: IP Org as rows, start_time as columns
        # https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
        pivotDF = aggregated.pivot_table(
            index=['domain', 'IP Org'],
            columns='start_time',
            values='t_vector',
            aggfunc='first'
        ).reset_index()


        return pivotDF
import pandas as pd

# Read the Excel files
edge_df = pd.read_excel('edge.xlsx')
active_df = pd.read_excel('active.xlsx')

# Initialize an empty DataFrame to store the results
result_df = pd.DataFrame(columns=['iteration', 'active_node_id', 'source', 'target'])

# Iterate over the active_df to find active nodes and their corresponding edges
for col in active_df.columns[1:]:  # Skipping the first column 'node_id'
    iteration = col.split('_')[-1]  # Extract the iteration number from the column name
    active_nodes = active_df[active_df[col] == 'active']['node_id'].tolist()
    
    for node in active_nodes:
        edges = edge_df[edge_df['source'] == node]
        edges['iteration'] = iteration
        edges['active_node_id'] = node
        result_df = pd.concat([result_df, edges[['iteration', 'active_node_id', 'source', 'target']]], ignore_index=True)

# Export the result to a new Excel file
result_df.to_excel('result.xlsx', index=False)

print("Result exported to 'result.xlsx'")

# Plot clusters with better styling
plt.figure(figsize=(8,6))

scatter = plt.scatter(
    data['AnnualIncome'],
    data['SpendingScore'],
    c=data['Cluster']
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation (KMeans)")

# Add legend
plt.legend(*scatter.legend_elements(), title="Clusters")

plt.grid(True)
plt.show()

# Cluster insights
print("\nCluster Summary:")
print(data.groupby('Cluster')[['AnnualIncome','SpendingScore']].mean())
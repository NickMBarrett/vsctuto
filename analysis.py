import pandas as pd
data = pd.read_csv('data/data.csv')

# Analyze cure rates for each treatment
cure_rates = data.groupby('Treatment')['Outcome'].apply(lambda x: (x == 'Cured').mean())

# Get placebo cure rate
placebo_rate = cure_rates.get('Placebo', 0)

# Compare drugs to placebo
best_drug = None
best_increase = 0
for drug in ['Drug A', 'Drug B', 'Drug C']:
    if drug in cure_rates:
        increase = cure_rates[drug] - placebo_rate
        if increase > best_increase and increase > 0:
            best_increase = increase
            best_drug = drug

# Write result to solution.txt
with open('solution.txt', 'w') as f:
    f.write(best_drug if best_drug else 'None')

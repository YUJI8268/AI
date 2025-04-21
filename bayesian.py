from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define the structure of the Bayesian Network
model = BayesianNetwork([('Rain', 'Traffic'), ('Traffic', 'Late to Work')])

# Step 2: Define the Conditional Probability Distributions (CPDs)
# CPD for 'Rain' (Rain has no parents)
cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.7], [0.3]]  # 70% No Rain, 30% Rain
)

# CPD for 'Traffic' given 'Rain'
cpd_traffic = TabularCPD(
    variable='Traffic',
    variable_card=2,
    values=[
        [0.8, 0.4],   # P(Traffic=Light | Rain=No), P(Traffic=Light | Rain=Yes)
        [0.2, 0.6]    # P(Traffic=Heavy | Rain=No), P(Traffic=Heavy | Rain=Yes)
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

# CPD for 'Late to Work' given 'Traffic'
cpd_late_to_work = TabularCPD(
    variable='Late to Work',
    variable_card=2,
    values=[
        [0.9, 0.6],   # P(Late=No | Traffic=Light), P(Late=No | Traffic=Heavy)
        [0.1, 0.4]    # P(Late=Yes | Traffic=Light), P(Late=Yes | Traffic=Heavy)
    ],
    evidence=['Traffic'],
    evidence_card=[2]
)

# Step 3: Add CPDs to the model
model.add_cpds(cpd_rain, cpd_traffic, cpd_late_to_work)

# Check if the model is valid
assert model.check_model(), "Model is incorrect!"

# Step 4: Perform inference
inference = VariableElimination(model)

# Query: P(Late to Work | Rain=Yes)
prob_late_given_rain = inference.query(variables=['Late to Work'], evidence={'Rain': 1})
print(prob_late_given_rain)

# Query: P(Traffic | Rain=No)
prob_traffic_given_rain = inference.query(variables=['Traffic'], evidence={'Rain': 0})
print(prob_traffic_given_rain)

# Query: P(Rain | Late to Work=Yes)
prob_rain_given_late = inference.query(variables=['Rain'], evidence={'Late to Work': 1})
print(prob_rain_given_late)

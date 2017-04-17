Manifest = {
'Name': 'com.test',
'Description': 'CPU',
'Version': '1.2',
'Author': 'Sonali R'
}
ParameterDefinitions = {
'low_threshold': {
'Name': 'High Threshold',
'Description': 'When the CPU crosses 80% diag dump will be collected',
'Type': 'integer',
'Default': 80
}
}
VariableDefinitions = {
'my_index': {
'Name': 'My Index',
'Description': 'Special index that I want to persist across sandbox executions'
}
}
class Policy(BasePolicy):
def __init__(self):
'''

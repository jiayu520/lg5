import yaml


def read_data(path):
    try:
         data = yaml.safe_load(open(path))
         # print(data)
         return data
    except Exception as e:
        print(e)
# read_data('../testdata/adddata.yml')
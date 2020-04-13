# thesis2020
Masters Thesis 2019 Deep Learning Testing Benchmarking 


# Latex Document Link

https://www.overleaf.com/project/5df966e2bdb0ce0001befe5e

# Task List
- [x] Document Results
- [x] 1st version of Benchmarking script
- [x] Task automation check
- [x] run config check
- [ ] Link all task
- [ ] Script Results

# -- Help
- Python and Libs
```
 alias python=/usr/local/bin/python2.7
 python2.7 -m pip install pytest --user
 python -m pip install bunch --user
 python -m pip install texttable --user
 ```
 
# run_config.json
```json
 {
   "toolName": "DeepXplore",                    
   "description": "Whitebox DL testing tool",
   "authors": "Din Lin",
   "language": "python",                       
   "publication": "2018", 
   "path_to_script" : "/Users/hchuphal/Desktop/github/thesis2020/Code/deepxplore-master",                    
   "commands": [
      { "path_1":"/Users/hchuphal/Desktop/github/thesis2020/Code/deepxplore-master/MNIST",
      "command_1": "python2.7 gen_diff.py occl -t 0 1.0 0.1 10 10 10 0",
      "dataset_type": "images"},
      {"path_2":"/Users/hchuphal/Desktop/github/thesis2020/Code/deepxplore-master/Driving",
      "command_2": "python2.7 gen_diff.py light 1 0.1 10 20 50 0",
      "dataset_type": "images"},
      {"path_3":"pass",
      "command_3": "pass",
      "dataset_type": "pass"},
      {"path_4":"pass",
      "command_4": "pass",
      "dataset_type": "pass"},
      {"path_5":"pass",
      "command_5": "pass",
      "dataset_type": "pass"},
      {"path_6":"pass",
      "command_6": "pass",
      "dataset_type": "pass"},
      {"path_7":"pass",
      "command_7": "pass",
      "dataset_type": "pass"}
   ],
   "manual_check": {
      "model_selection" : "No",
      "retraining" : "No",
      "differential_testing" : "No"
   },
   "datasets_classification": [
      {"images" : "No"},
      {"self_driving" : "No"},
      {"texts" : "No"}
   ],
   "output_config" : [
      {"output_saved" : "No"},
      {"output_default_path" : "_path_"},
      {"postProcessingCommand" : "No"},
      {"parser_path" : "_path_"}
   ]
}
```

# Run commands :
```
 python benchmarking_tasks.py 1 3
```

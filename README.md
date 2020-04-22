# Masters Thesis, Chalmers|GU, Gothenburg, Sweden, 2020

**Benchmarking Deep Learning Testing Techniques,**

# Authors :
```
Himanshu Chuphal <guschuhi@student.gu.se>, N2COS
Kristiyan Dimitrov <gusdimkr@student.gu.se>, N2SOF

Supervisor : Robert Feldt, CSE Dept, Chalmers[ GU
```

# Run as:
```
python2.7 dl_benchmarking_main.py
```
- or run Benchmarking tasks directly:
```
 python2.7 benchmarking_tasks.py
```
- and Select an option as given below from the comnand line ::

```
+--------------------------------------+
|                                      |
|      DL Testing Tools Benchmarking   |
|                                      |
|            Masters Thesis            |
|                                      |
+--------------------------------------+


Welcome : Input options to run DL benchmakring tasks >>

 Select an option to run Benchmarking method >>
1. Fill out Tool Run Config >>
2. Check Tool's Run Config
3. Install Requirements
4. Execute Benchmarking Tasks (7)
5. Tasks Info
6. DL Testing Tools List
7. Check Version of the tool
8. -- Help??
9. EXIT


Enter an option to run the tool [ 1-8 ] = 3

```

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
      {"path_2":"/Users/hchuphal/Desktop/github/thesis2020/Code/deepxplore-master/PDF/",
      "command_2": "python2.7 gen_diff.py 2 0.1 10 20 50 0",
      "dataset_type": "texts"},
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
      "retraining" : "Yes",
      "differential_testing" : "Yes"
   },
   "datasets_classification": {
      "images" : "Yes",
      "self_driving" : "Yes",
      "texts" : "No"
   },
   "output_config" : {
      "output_saved" : "Yes",
      "output_default_path" : "_path_",
      "postProcessingCommand" : "None",
      "parser_path" : "_path_"
   }
}
```
# Activate Config for a Required Test

```
# RUN CONFIG for DL TESTING TOOLS
#_DEFAULT_RUN_CONFIG = 'run_config1.json'
#_DEFAULT_RUN_CONFIG = 'run_config_deepX.json'     # _DEEPXPLORE_RUN_CONFIG
#_DEFAULT_RUN_CONFIG = 'run_config_dlfuzz.json'    # _DLFUZZ_RUN_CONFIG
#_DEFAULT_RUN_CONFIG = 'run_config_deepfault.json' # _DEEPFAULT_RUN_CONFIG
_DEFAULT_RUN_CONFIG = 'run_config_sadl.json'       # _SADL_RUN_CONFIG

```


 # end

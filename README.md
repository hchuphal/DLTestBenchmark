# Masters Thesis Jan- May, 2020 

**Benchmarking Deep Learning Testing Techniques**

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
**************************************************
Check the run Config of the DL testing tool before starting Benchmarking Tasks...
**************************************************


Welcome : Input options to run DL benchmakring tasks >>

 Select an option to run Benchmarking method >>
1. Fill out Tool Run Config >>
2. Check Tool's Run Config
3. Execute Benchmarking Tasks (7)
4. Tasks Info
5. DL Testing Tools List
6. Check Version of the tool
7. -- Help??
8. EXIT
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
 # end

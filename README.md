# DLTestBenchmark Version 1.0, Chalmers|GU, Gothenburg, Sweden, 2020

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

# About the Benchmarking Tool
- [x] Version. : 1.0
- [x] Benchmarking models included
- [x] Run and Configuration help file ( inside /script)
- [x] Example Run and Configuration File
- [X] Execution commands

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
   "toolName": "DeepFault",                    
   "description": "DeepFault: Fault Localization for Deep Neural Networks",
   "authors": "Hasan Ferit Eniser, Simos Gerasimou, Alper Sen",
   "language": "python",                       
   "publication": "2019",
   "path_to_script" : "/Users/hchuphal/Desktop/github/thesis2020/Code/DeepFault-master",                    
   "commands": [
      { "path_1":"/Users/hchuphal/Desktop/github/thesis2020/Code/DeepFault-master",
      "command_1": "python2.7 run.py --model mnist_test_model_1_100 --dataset mnist -C 9 --approach tarantula --suspicious_num 10",
      "dataset_type": "images"},
      {"path_2":"/Users/hchuphal/Desktop/github/thesis2020/Code/DeepFault-master",
      "command_2": "python2.7 run.py --model cifar10_test_model_1_512_leaky_relu --dataset cifar10 -C 9 --approach tarantula --suspicious_num 10",
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
      "model_selection" : "Yes",
      "retraining" : "Yes",
      "differential_testing" : "No"
   },
      "benchmarking_commands": [
      { "path_1":"/Users/hchuphal/Desktop/github/thesis2020/Code/DeepFault-master",
      "command_1": "python2.7 run.py --model Images_cifar10_1_512_leaky_relu_model1 --dataset cifar10 -C 9 --approach tarantula --suspicious_num 10",
      "dataset_type": "images"},
      {"path_2":"/Users/hchuphal/Desktop/github/thesis2020/Code/DeepFault-master",
      "command_2": "python2.7 run.py --model Self_Driving_CNN_model1 --dataset nvidia -C 9 --approach tarantula --suspicious_num 10",
      "dataset_type": "self_driving"},
      { "path_3":"/Users/hchuphal/Desktop/github/thesis2020/Code/DeepFault-master",
      "command_3": "python2.7 run.py --model Text_imdb_CNN_model2 --dataset imdb -C 9 --approach tarantula --suspicious_num 10",
      "dataset_type": "texts"},
      {"path_4":"pass",
      "command_4": "pass",
      "dataset_type": "images"}
   ],
   "datasets_classification": {
      "images" : "Yes",
      "self_driving" : "No",
      "texts" : "No"
   },
   "output_config" : {
      "output_saved" : "Yes",
      "output_default_path" : "./output/",
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
# Flow :
![image info](./scripts/flow.png)

# Results
![image info](./scripts/a1.png)


 # end

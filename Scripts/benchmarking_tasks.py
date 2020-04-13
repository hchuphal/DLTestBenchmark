##############################################################################################
#
# Description : DL Testing Benchmarking Python tool to perform benchmakring tasks
# Input  : models and datasets
# Output :  Output of all 7 tasks
# Usage : python2.7 benchmarking_tasks.py
# Author : Himanshu
#
##############################################################################################
#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import unittest.runner
import itertools
import collections
import sys
import argparse
import os
import shutil
import errno
import json
import subprocess
import platform
import time, timeit
import logging
import sys
import logging

# Set up logging and formatting
logger = logging.getLogger()
logFormatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Set up the console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# Set up the file handler 
fileHandler = logging.FileHandler("{0}/{1}.log".format('.', 'benchmarking_tasks'))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

# Set up logging levels
consoleHandler.setLevel(logging.INFO)
fileHandler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)

## macros

_DEFAULT_RUN_CONFIG = 'run_config1.json'
_TEMP_DIR = './temp/'
_TEMP_CONFIG = './temp/run_config_tool.json'

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start) * 1000.0
        logger.warning('Benchmarking Profiling : ' + self.name + ' took: ' + str(self.took) + ' ms')


class BenchmakringTasksResults(unittest.runner.TextTestResult):
    """Extension of TextTestResult to support numbering test cases"""

    def __init__(self, stream, descriptions, verbosity):
        """Initializes the test number generator, then calls super impl"""

        self.test_numbers = itertools.count(1)

        return super(BenchmakringTasksResults, self).__init__(stream, descriptions, verbosity)

    def startTest(self, test):
        """Writes the test number to the stream if showAll is set, then calls super impl"""

        if self.showAll:
            progress = '[{0}/{1}] '.format(next(self.test_numbers), self.test_case_count)
            self.stream.write(progress)

            # Also store the progress in the test itself, so that if it errors,
            # it can be written to the exception information by our overridden
            # _exec_info_to_string method:
            test.progress_index = progress

        return super(BenchmakringTasksResults, self).startTest(test)

    def _exc_info_to_string(self, err, test):
        """Gets an exception info string from super, and prepends 'Test Number' line"""

        info = super(BenchmakringTasksResults, self)._exc_info_to_string(err, test)

        if self.showAll:
            info = 'Test number: {index}\n{info}'.format(
                index=test.progress_index,
                info=info
            )

        return info


class BenchmarkingTasksRunner(unittest.runner.TextTestRunner):
    """Extension of TextTestRunner to support numbering test cases"""

    resultclass = BenchmakringTasksResults

    def run(self, test):
        """Stores the total count of test cases, then calls super impl"""

        self.test_case_count = test.countTestCases()
        return super(BenchmarkingTasksRunner, self).run(test)

    def _makeResult(self):
        """Creates and returns a result instance that knows the count of test cases"""

        result = super(BenchmarkingTasksRunner, self)._makeResult()
        result.test_case_count = self.test_case_count
        return result


class BenchmarkingTasks(unittest.TestCase):
    """Dummy test case to illustrate usage"""

    fail_1 = 0
    fail_2 = 0

    def setUp(self):
        self.a = 1
        self._pass = ['yes', 'Yes', 'y', 'Y', 'YES']
        self._fail = ['no', 'No', 'n', 'N', 'NO']
        self._languages = ['python', 'Python', 'PYTHON']
        self.manual_check = sys.argv[1]
        self.output_config = sys.argv[2]
        self.datasets = sys.argv[3]
        self.language = sys.argv[4]
        self._os = platform.system()
        self._time = sys.argv[5]

    def task_1(self):
        time.sleep(1)
        #print self.manual_check['model_selection']
        assert self.manual_check['model_selection']  in self._pass, "Model Selection is not possible"

    def task_2_1(self):
        time.sleep(1)
        assert self.datasets['images']  in self._pass, "Image Classifications are not possible"

    def task_2_2(self):
        time.sleep(1)
        assert self.datasets['self_driving']  in self._pass, "Self_driving datasets are not possible"

    def task_2_3(self):
        time.sleep(1)
        assert self.datasets['texts']  in self._pass, "Texts/Malware datasets are not possible"

    def task_3(self):
        time.sleep(1)
        assert self.manual_check['retraining']  in self._pass,"Retraining is not possible"

    def task_4(self):
        time.sleep(1)
        assert self.manual_check['differential_testing'] in self._pass,"Differential Testing is not possible"

    def task_5(self):
        time.sleep(1)
        assert self._time > 1000.0 ,"Execution time of Testing is less than 1 second"
        #logger.info("\n Total time taken in ms : " + str(self._time))

    def task_6(self):
        time.sleep(1)
        assert self.output_config['output_saved'] in self._pass,"Output Saving is NOT possible"

    def task_7(self):
        time.sleep(1)
        # print self._os #Linux: Linux Mac: Darwin Windows: Windows
        assert self.language in self._languages,"Not support in this OS: " + str(self._os)


def get_tests():
    task_funcs = ['task_1', 'task_2_1', 'task_2_2', 'task_2_3', 'task_3', 'task_4', 'task_5', 'task_6', 'task_7']
    return [BenchmarkingTasks(func) for func in task_funcs]

def _make_runconfig():
    try:
        os.makedirs(_TEMP_DIR)    
        #print("Directory " , dirName ,  " Created ")
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
 
    shutil.copy2(_DEFAULT_RUN_CONFIG, './temp/run_config_tool.json')

if __name__ == '__main__':
    # 1. get run config
    _make_runconfig()
    
    sys.stdout = open('Benchmarking_console_log.txt', 'w')
    # 2. Read the run config
    if _TEMP_CONFIG:
        with open(_TEMP_CONFIG, 'r') as myfile:
            json_data=myfile.read()
    parsed_json = (json.loads(json_data))
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))
    obj = json.loads(json_data)

    language = str(obj['language'])
    commmands_list = obj['commands']
    manual_check = obj['manual_check']
    output_config = obj['output_config']
    language = obj['language']
    datasets = obj['datasets_classification']
    spath = str(obj['path_to_script'])
    _total_commands = [command for command in commmands_list if command["dataset_type"] != 'pass']
    logger.info("\n")
    logger.info ("\n********* Tasks Execution Started ...... *********")
    logger.info('Total ' + str(len(_total_commands))+ ' commands to execute for Benchmarking!\n\n')
    start = time.time()
    for i, commands in enumerate(commmands_list): 
        for command, argument  in commands.items():
            if argument != 'pass':
                logger.info('Executing DL Testing tool ' +'run ' + command +' : '+ argument)
                if 'dataset_type' in ['images', 'texts', 'self_driving']:
                    logger.info('Dataset Classifications'+ dataset_type)
                    # change to working directory of the script
                os.chdir(commands["path_"+str(i+1)])
                if "python" in argument:
                    with CodeTimer(' Time to run the  testing command :'):
                        os.system(argument)
                    #returned_output = subprocess.check_output('python gen_diff.py light 1 0.1 10 20 50 0')
    final_time = (time.time() - start) * 1000.0
    print("\n")
    logger.info("Total Execution Time taken to run all the commands :" +str(final_time) +' ms')
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='My Input')
    parser.add_argument('filename', default='some_file.txt')
    parser.add_argument('unittest_args', nargs='*')
    #parser.add_argument('--name', required=True)
    args = parser.parse_args()
    #sys.argv[1:] = args.unittest_args
    sys.argv[1:] = [manual_check, output_config, datasets, language, final_time]
    test_suite = unittest.TestSuite()

    repetitions = 1  # how many times to we want to repeat the tasks (7)
    tasks = get_tests()
    for __ in xrange(0, repetitions):
        test_suite.addTests(tasks)
    logger.info("\nBenchmarking Tasks Execution Start....")
    time.sleep(1)
    BenchmarkingTasksRunner(verbosity=2).run(test_suite)
    time.sleep(1)
    # post processing of results--- optional
    logger.info("Post processing of result Support :"+ output_config['postProcessingCommand']+'\n')
    if output_config['postProcessingCommand'] != 'None':
        logger.info(" Details of Post processing script :")
        logger.info("Saved Output Path :" + output_config['output_default_path'])
        logger.info("Command :" + output_config['postProcessingCommand'])
        logger.info("Parse path :" + output_config['parser_path']+'\n')

    
    logger.info("********* Tasks Execution Completed Successfully! ********* \n")

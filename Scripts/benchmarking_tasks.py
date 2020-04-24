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
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import unittest, unittest.runner
import itertools, collections
import argparse, errno
import time, timeit, sys, platform, subprocess, os
import logging, shutil, json
import TestRunner, progressbar 
from datetime import datetime

# Set up logging and formatting
logger = logging.getLogger()
logFormatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Set up the console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# Set up the file handler 
fileHandler = logging.FileHandler("{0}/{1}.log".format('.', 'benchmarking_tasks_console'))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

# Set up logging levels
consoleHandler.setLevel(logging.INFO)
fileHandler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)

# /Applications/Netron.app/Contents/MacOS/Netron generate neural_networks/benchmarking.h5 b.jpg

# RUN CONFIG for DL TESTING TOOLS
#_DEFAULT_RUN_CONFIG = 'run_config1.json'
#_DEFAULT_RUN_CONFIG = 'run_config_deepX.json'      # _DEEPXPLORE_RUN_CONFIG
#_DEFAULT_RUN_CONFIG = 'run_config_dlfuzz.json'     # _DLFUZZ_RUN_CONFIG
#_DEFAULT_RUN_CONFIG = 'run_config_sadl.json'       # _SADL_RUN_CONFIG
_DEFAULT_RUN_CONFIG = 'run_config_deepfault.json'  # _DEEPFAULT_RUN_CONFIG


_TEMP_DIR = './temp/'
_TEMP_CONFIG = './temp/run_config_tool.json'
_OUTPUT = 'output'
_buffer = []
_ben_buffer = []
final_time = 0.0

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start)
        logger.warning('Benchmarking Profiling : ' + self.name + ' took: ' + str(self.took) + ' Seconds')


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
            info = 'Benchmarking Task number: {index}\n{info}'.format(
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
    """ Results of 7 Tasks"""

    def setUp(self):
        #print "Executing ", self._testMethodName
        self._pass = ['yes', 'Yes', 'y', 'Y', 'YES']
        self._fail = ['no', 'No', 'n', 'N', 'NO']
        self._languages = ['python', 'Python', 'PYTHON', 'perl', 'erlang', 'java']
        self.manual_check = manual_check
        self.output_config = output_config
        self.datasets = datasets
        self.language = language
        self._os = platform.system()
        self._time = final_time
        self._command_status = _buffer
        self._ben_c = ben_commmands_list
        self._ben_buffer_img = _ben_buffer_img
        self._ben_buffer_sd =_ben_buffer_sd
        self._ben_buffer_tex = _ben_buffer_tex
       
    def test_Model_Selection(self):
        time.sleep(0.2)
        assert self.manual_check['model_selection']  in self._pass, "Model Selection is not possible"

    def test_Image_Classifications_Support(self):
        time.sleep(0.2)
        assert self.datasets['images']  in self._pass, "Image Classifications are not possible"
        for i, status in enumerate(self._ben_buffer_img):
            if self._ben_buffer_img[i] == 0 and str(self.manual_check['model_selection']).lower() == 'yes':
                print("With Image Classifications Model:Images_cifar10_1_512_leaky_relu_model1")
            elif self._ben_buffer_img[i] != 0 and str(self.manual_check['model_selection']).lower() == 'yes':
                print("Execution Failed with Model:Images_cifar10_1_512_leaky_relu_model1")
                assert self._ben_buffer_img[i] == 0, "DL Testing tool failed on Images_cifar10_1_512_leaky_relu_model1"

    def test_SelfDriving_Classifications_Support(self):
        time.sleep(0.2)
        assert self.datasets['self_driving']  in self._pass, "Self_driving datasets are not possible"
        for i, status in enumerate(self._ben_buffer_sd):
            if self._ben_buffer_sd[i] == 0 and str(self.manual_check['model_selection']).lower() == 'yes':
                print("Execution Failed with Model:Self_Driving_CNN_model1")
            elif self._ben_buffer_sd[i] != 0 and str(self.manual_check['model_selection']).lower() == 'yes':
                print("With Self_driving Classifications Model:Self_Driving_CNN_model1")
                assert self._ben_buffer_sd[i] == 0, "DL Testing tool failed on Self_Driving_CNN_model1"

    def test_Texts_Classifications_Support(self):
        time.sleep(0.2)
        assert self.datasets['texts']  in self._pass, "Texts/Malware datasets are not possible"
        for i, status in enumerate(self._ben_buffer_tex):
            if self._ben_buffer_tex[i] == 0 and str(self.manual_check['model_selection']).lower() == 'yes':
                print("Executing Failed with Texts Classifications Model:Text_imdb_CNN_model2")
            elif self._ben_buffer_tex[i] != 0 and str(self.manual_check['model_selection']).lower() == 'yes':
                print("With Texts Classifications Model:Text_imdb_CNN_model2")
                assert self._ben_buffer_tex[i] == 0, "DL Testing tool failed on Text_imdb_CNN_model2"

    def test_Retraining(self):
        time.sleep(0.2)
        assert self.manual_check['retraining']  in self._pass,"Retraining is not possible"

    def test_Differential_Testing(self):
        time.sleep(0.2)
        assert self.manual_check['differential_testing'] in self._pass,"Differential Testing is not possible"

    def test_Execution_Time(self):
        time.sleep(0.2)
        formatted_time = "{:.2f}".format(self._time)
        assert self._time > 10.0 ,"Execution time of Testing is less than 10 second"
        print(str(formatted_time)+ ' Seconds')
        #logger.info("\n Total time taken in ms : " + str(self._time))

    def test_Output_Capabilities(self):
        time.sleep(0.2)
        assert self.output_config['output_saved'] in self._pass,"Output Saving is NOT possible"
        #logger.info(self._command_status)
        for i, status in enumerate(self._command_status):
            if self._command_status[i] != 0:
                assert self._command_status[i] == 0, "DL Testing Tool command failed to execute!"

    def test_OS_Support(self):
        # print self._os #Linux: Linux Mac: Darwin Windows: Windows
        assert self.language in self._languages,"Not support in this OS: " + str(self._os)

def get_tests():
    #task_funcs = ['task_1', 'task_2_1', 'task_2_2', 'task_2_3', 'task_3', 'task_4', 'task_5', 'task_6', 'task_7']
    task_funcs = ['test_Model_Selection', 'test_Image_Classifications_Support', 'test_SelfDriving_Classifications_Support', 'test_Texts_Classifications_Support', 'test_Retraining', 'test_Differential_Testing', 'test_Execution_Time', 'test_Output_Capabilities', 'test_OS_Support']
    return [BenchmarkingTasks(func) for func in task_funcs]

def _make_runconfig():
    try:
        os.makedirs(_OUTPUT)    
        #print("Directory " , dirName ,  " Created ")
    except OSError as e:
        if e.errno == errno.EEXIST:
            logger.warning('Output Config :: Already Exist!')
 
    shutil.copy2(_DEFAULT_RUN_CONFIG, './temp/run_config_tool.json')

def _write_output(_buffer):
    logger.info(_buffer)
    try:
       # log file to write to
       logFile = _OUTPUT+'Benchmarking_dl_testing_tool_'+time.strftime("%Y%m%d-%H%M%S")+'_._log'
       report = open(logFile, 'a')
       report.write(_buffer)

    except Exception as e:
       # get line number and error message
       report.write('En error message while Executing DL Testing command' + e+ logFile)

if __name__ == '__main__':
    # 1. get run config
    _make_runconfig()
    try:
        shutil.rmtree(_OUTPUT)
        os.mkdir(_OUTPUT)
    except OSError as e:
        logger.warning("Error: No Previous Output found! %s - %s." % (e.filename, e.strerror))
    #sys.stdout = open('Benchmarking_logs_'+time.strftime("%Y%m%d-%H%M%S"+'_.log'), 'w')
    # 2. Read the run config
    if _TEMP_CONFIG:
        with open(_TEMP_CONFIG, 'r') as myfile:
            json_data=myfile.read()
    parsed_json = (json.loads(json_data))
    obj = json.loads(json_data)

    language = str(obj['language'])
    commmands_list = obj['commands']
    manual_check = obj['manual_check']
    output_config = obj['output_config']
    language = obj['language']
    datasets = obj['datasets_classification']
    ben_commmands_list = obj['benchmarking_commands']
    # 3. Run each command specified in the run configuration of the DL testing tool
    spath = str(obj['path_to_script'])
    _total_commands = [command for command in commmands_list if command["dataset_type"] != 'pass']
    _total_ben_commands = [command for command in commmands_list if command["dataset_type"] != 'pass']
    logger.info("\n")
    logger.info ("\n********* Tasks Execution Started ...... *********")
    logger.info('Total ' + str(len(_total_commands))+ ' commands to execute for Benchmarking!\n\n')
    #_buffer = []
    bar = progressbar.ProgressBar(maxval=9, \
    widgets=[progressbar.Bar('#', 'Progress ....[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    start = time.time()
    for i, commands in enumerate(commmands_list): 
        for command, argument  in commands.items():
            if argument != 'pass':
                logger.info('Executing DL Testing tool on default Models ' +'run ' + command +' : '+ argument)
                if 'dataset_type' in ['images', 'texts', 'self_driving']:
                    logger.info('Dataset Classifications'+ dataset_type)
                    # change to working directory of the script
                os.chdir(commands["path_"+str(i+1)])
                if "python" in argument:
                    with CodeTimer(' Time to run the  testing command :'):
                        try:
                            _status = os.system(argument)
                            _buffer.append(_status)
                            #_buffer = subprocess.check_output(argument)
                            #_write_output(_buffer)
                        except Exception as e:
                            logger.error("Benchmarking DL Testing Tool command failed!")
    # 3 Run on Benchmarking models
    ic = tc = sdc = 0
    _ben_buffer_img = []
    _ben_buffer_sd = []
    _ben_buffer_tex = []
    if str(manual_check['model_selection']).lower() == 'yes':
        logger.info('Total ' + str(len(_total_ben_commands))+ ' commands to execute for Benchmarking Models!\n\n')
        for i, commands in enumerate(ben_commmands_list): 
            for command, argument  in commands.items():
                if argument != 'pass':
                    logger.info('Executing DL Testing tool on Benchmarking Models ' +'run ' + command +' : '+ argument)
                    if 'dataset_type' in ['images', 'texts', 'self_driving']:
                        logger.info('Dataset Classifications'+ dataset_type)
                        # change to working directory of the script
                    if str(commands["path_"+str(i+1)]).lower() != 'pass':
                        os.chdir(commands["path_"+str(i+1)])
                    if "python" in argument:
                        with CodeTimer(' Time to run the  testing command :'):
                            try:
                                if str(datasets['images']).lower() == 'yes' and \
                                    ic != 1:
                                    #_images_command = _ben_images = 
                                    _ben_status = os.system(argument)
                                    _ben_buffer_img.append(_ben_status)
                                    ic = 1
                                elif str(datasets['self_driving']).lower() == 'yes' and \
                                    sdc != 1:
                                    _ben_status = os.system(argument)
                                    _ben_buffer_sd.append(_ben_status)
                                    sdc = 1
                                elif str(datasets['texts']).lower() == 'yes' and \
                                    tc != 1:
                                    _ben_status = os.system(argument)
                                    _ben_buffer_tex.append(_ben_status)
                                    tc = 1
                                else:
                                    ben_command = 'Command NOT Supported!'
                            except Exception as e:
                                logger.error("Benchmarking DL Testing Tool command failed!")

    final_time = (time.time() - start)
    bar.finish()
    print("\n")
    logger.info("Total Execution Time taken to run all the commands :" +str(final_time) +' Seconds')
    parser = argparse.ArgumentParser()
    #parser.add_argument('discover', default='discover')
    #parser.add_argument('filename', default='some_file.txt')
    #parser.add_argument('unittest_args', nargs='*')
    #parser.add_argument('--name', required=True)
    #args = parser.parse_args()
    #sys.argv[1:] = args.unittest_args
    #sys.argv[1:] = [manual_check, output_config, datasets, language, final_time, _buffer]
    test_suite = unittest.TestSuite()

    repetitions = 1  # how many times to we want to repeat the tasks (7)
    tasks = get_tests()
    for __ in xrange(0, repetitions):
        test_suite.addTests(tasks)
    logger.info("\nExecuting Benchmakring Tasks one by one....")
    time.sleep(1)
    TestRunner.main()
    #BenchmarkingTasksRunner(verbosity=2).run(test_suite)
    runner.run(test_suite)
    final_time_2 = (time.time() - start)
    logger.info("Total Execution Time taken by Benchmakring Tool :" +str(final_time_2) +' Seconds')
    time.sleep(1)
    # post processing of results--- optional
    logger.info("Post processing of result Support :"+ output_config['postProcessingCommand']+'\n')
    if output_config['postProcessingCommand'] != 'None':
        logger.info(" Details of Post processing script :")
        logger.info("Saved Output Path :" + output_config['output_default_path'])
        logger.info("Command :" + output_config['postProcessingCommand'])
        logger.info("Parse path :" + output_config['parser_path']+'\n')  
    logger.info("********* Tasks Execution Completed Successfully! ********* \n")
    #end
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on July 02, 2021, at 17:31
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'AL'  # from the Builder filename that created this script
expInfo = {'participant*': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant*'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\Project BL\\Aging Study\\Agingstudy_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1504, 1003], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome0"
Welcome0Clock = core.Clock()
Welcome0Mssg = visual.TextStim(win=win, name='Welcome0Mssg',
    text="Welcome to the experiment!\n\n\n\nThis experiment involves audio stimuli and requires you to wear headphones. Before we begin, please make sure that you're in a quiet listening environment, that you are wearing headphones, and that your volume is turned on.\n\n\n\nPress SPACE to begin",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Welcome0Continue = keyboard.Keyboard()

# Initialize components for Routine "SoundCheckIntro"
SoundCheckIntroClock = core.Clock()
SoundCheckTxt = visual.TextStim(win=win, name='SoundCheckTxt',
    text='We will begin with a quick volume calibration and headphone check. \n\nFirst, we will play some music to make sure that your sound volume is at a comfortable level.\n\n\n\nPress SPACE to begin the volume calibration ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
SoundCheckBegin = keyboard.Keyboard()

# Initialize components for Routine "SoundCheck"
SoundCheckClock = core.Clock()
VolumeAdjust = sound.Sound('volumeadjust.wav', secs=-1, stereo=True, hamming=True,
    name='VolumeAdjust')
VolumeAdjust.setVolume(0.4)
SoundCheckEndTxt = visual.TextStim(win=win, name='SoundCheckEndTxt',
    text='Please adjust your volume to a comfortable level.\n\n\n\nPress SPACE when you are ready to continue ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
SoundCheckEndKey = keyboard.Keyboard()

# Initialize components for Routine "HeadphoneCheck"
HeadphoneCheckClock = core.Clock()
HeadphoneCheckTxt = visual.TextStim(win=win, name='HeadphoneCheckTxt',
    text='Next, we will do a short headphone check. Your submission may be rejected if you fail the headphone check.\n\nOn each trial, you will hear three tones. One of these tones will be quieter than the others. You will identify whether the quiet tone occurred first, second, or third.\n\nThere are six trials in total.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
HeadphoneContinue = visual.TextStim(win=win, name='HeadphoneContinue',
    text='Press SPACE to begin the headphone check',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
HeadphoneContinueKey = keyboard.Keyboard()

# Initialize components for Routine "HeadphonePlay"
HeadphonePlayClock = core.Clock()
CheckSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='CheckSound')
CheckSound.setVolume(1)
CheckTxt = visual.TextStim(win=win, name='CheckTxt',
    text='Which tone was the quietest?\n(Press the corresponding number on your keyboard)\n\n1 = First  2 = Second  3 = Third',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CheckResp = keyboard.Keyboard()
TrialNumber = visual.TextStim(win=win, name='TrialNumber',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
counter = 1
checkcount = str(counter) + "/6"
Cross2 = visual.TextStim(win=win, name='Cross2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "HeadphoneFeedback"
HeadphoneFeedbackClock = core.Clock()
FeedbackMssg = visual.TextStim(win=win, name='FeedbackMssg',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MSTWelcome"
MSTWelcomeClock = core.Clock()
MSTWelcomeTxt = visual.TextStim(win=win, name='MSTWelcomeTxt',
    text='Task A (20 minutes)\n\nResearchers in XXX University are studying alien words and have created a sound file for each word they have collected. However, some of the sound files have been accidentally duplicated and now they need your help looking for the duplicated words.\n\nThere are 100 sound files in total but almost half of them are duplicates. Your task is to listen to each word and label them as either "OLD" (duplicate) or "NEW".',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
WelcomeP2Continue = visual.TextStim(win=win, name='WelcomeP2Continue',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ContinueKey8 = keyboard.Keyboard()

# Initialize components for Routine "MSTWelcome2"
MSTWelcome2Clock = core.Clock()
MSTWelcome2Txt = visual.TextStim(win=win, name='MSTWelcome2Txt',
    text='It is important to note that some of the words are similar but not identical. Pay close attention to each word and only label it as "OLD" if it is EXACTLY THE SAME as a previous word.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTWelcomeCont = visual.TextStim(win=win, name='MSTWelcomeCont',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
MSTWelcomeContKey = keyboard.Keyboard()

# Initialize components for Routine "MSTTrainIntro"
MSTTrainIntroClock = core.Clock()
MSTTrainIntroTxt = visual.TextStim(win=win, name='MSTTrainIntroTxt',
    text='We will first begin with a few practice trials to familiarize you with the task. During the practice, we will give you the correct answer.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTTrainIntroCont = visual.TextStim(win=win, name='MSTTrainIntroCont',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
MSTTrainIntroKey = keyboard.Keyboard()
Tcount = 1
MSTTrialCount = 'Trial ' + str(Tcount)



# Initialize components for Routine "Pause1sec"
Pause1secClock = core.Clock()
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MSTTrain"
MSTTrainClock = core.Clock()
MSTTrainSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='MSTTrainSound')
MSTTrainSound.setVolume(1)
MSTTrainCross = visual.TextStim(win=win, name='MSTTrainCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
MSTTrainTrialNum = visual.TextStim(win=win, name='MSTTrainTrialNum',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "MSTTrainFeedback"
MSTTrainFeedbackClock = core.Clock()
MSTTrainOptions = visual.TextStim(win=win, name='MSTTrainOptions',
    text='1 = OLD      2 = NEW',
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
MSTTrainMssg = visual.TextStim(win=win, name='MSTTrainMssg',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
MSTTrainContinueMssg = visual.TextStim(win=win, name='MSTTrainContinueMssg',
    text='Press the correct number on your keyboard',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
MSTTrainKeys = keyboard.Keyboard()
MSTTrainCross2 = visual.TextStim(win=win, name='MSTTrainCross2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "MSTTestStartInstrct"
MSTTestStartInstrctClock = core.Clock()
MSTTestBeginTxt = visual.TextStim(win=win, name='MSTTestBeginTxt',
    text='Great job! This is the end of the practice.\n\n\nWe will now begin the actual task. There are 100 sound files in total. The words from the practice are not part of the actual task. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTTestBeginKey = keyboard.Keyboard()
MSTTestBegin = visual.TextStim(win=win, name='MSTTestBegin',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "MSTTrialCount"
MSTTrialCountClock = core.Clock()
Cross1500ms = visual.TextStim(win=win, name='Cross1500ms',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTcount = 0

# Initialize components for Routine "MSTplay"
MSTplayClock = core.Clock()
MSTTestOptions = visual.TextStim(win=win, name='MSTTestOptions',
    text='(Press the corresponding number on your keyboard)\n\n1 = OLD (The exact same word has been played before)\n\n2 = NEW (This word is being played for the first time)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTTestPlay = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='MSTTestPlay')
MSTTestPlay.setVolume(1)
MSTTestOptionKeys = keyboard.Keyboard()
MSTTestTrialNum = visual.TextStim(win=win, name='MSTTestTrialNum',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
MSTTestNote = visual.TextStim(win=win, name='MSTTestNote',
    text='*Words that are similar to but different from previously played words should also be labeled as NEW\n\n',
    font='Arial',
    pos=(0, -0.35), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "SLWelcome"
SLWelcomeClock = core.Clock()
WelcomeMssg = visual.TextStim(win=win, name='WelcomeMssg',
    text='Task B (35 minutes)\n\nResearchers from ZZZ University have recently collected some recordings of an alien speech from another planet. The speech consists of syllables that sound similar to English. The researchers need your help to study this speech. \n\nYou will first listen to a 6-minute recording of this speech and then complete three different tasks. In total, the study will take approximately 35 minutes to complete. You will be able to take short breaks in between tasks. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueButton = keyboard.Keyboard()
ContinueTxt = visual.TextStim(win=win, name='ContinueTxt',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ExposurePrep"
ExposurePrepClock = core.Clock()
# Choose the scrambling condition file
import random
c = random.randint(1, 3)
c = 1
cond = str(c) # Used as the file for the PlayTD loop



ExposureIntro = visual.TextStim(win=win, name='ExposureIntro',
    text='First, we will play a recording of this alien speech for 6 minutes with a short break every 2 minutes. \n\nThe recording is a little broken and the speech will stop playing from time to time. Please help the researchers mark the broken parts by pressing SPACE whenever the speech stops.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ExposureIntroKey = keyboard.Keyboard()
ExposureIntroCont = visual.TextStim(win=win, name='ExposureIntroCont',
    text='Press SPACE when you are ready to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Exposure"
ExposureClock = core.Clock()
scounter = 0
takebreak = 0
pausecheck = 0
volume0 = 1
volumecounter0 = 0
ExposurePlay = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='ExposurePlay')
ExposurePlay.setVolume(1.0)
ExposureCross = visual.TextStim(win=win, name='ExposureCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ExposureInstruction = visual.TextStim(win=win, name='ExposureInstruction',
    text='Press SPACE as soon as you can when the speech stops',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
PauseCheckKey = keyboard.Keyboard()
PauseCross = visual.TextStim(win=win, name='PauseCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
PauseInstruction = visual.TextStim(win=win, name='PauseInstruction',
    text='Press SPACE as soon as you can when the speech stops',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "TakeABreak"
TakeABreakClock = core.Clock()
BreakRespSubmit = keyboard.Keyboard()
BreakTxt = visual.TextStim(win=win, name='BreakTxt',
    text="Let's take a break.\n\n\nHow many different syllables do you think were in the speech? Click the box below to type your response.\n(Press ENTER to submit your answer)",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
BreakResponse = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0, -0.2),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='BreakResponse',
     autoLog=True,
)

# Initialize components for Routine "BreakOver"
BreakOverClock = core.Clock()
EndBreakInstruction = visual.TextStim(win=win, name='EndBreakInstruction',
    text="Let's take a break.\n\nYou can press SPACE whenever you are ready to return to the task.\nThe task will resume automatically after 30 seconds.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EndBreakKey = keyboard.Keyboard()

# Initialize components for Routine "Part1Intro"
Part1IntroClock = core.Clock()
WelcomeTxt2 = visual.TextStim(win=win, name='WelcomeTxt2',
    text="In the next part, you will complete different tasks using your experience with the alien speech.\n\nFirst, the researchers would like you to mark the timing of when each syllable appears in the speech.\n\nWe will play you 36 short snippets of the speech. At the beginning of each recording, you will be given a 'Target Syllable'. Every time the target syllable appears in the recording, press SPACE as quickly and accurately as you can to record the precise syllable onset time.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
BeginTxt = visual.TextStim(win=win, name='BeginTxt',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ContinueKey3 = keyboard.Keyboard()
repeatCount = 0
count = 0




# Initialize components for Routine "TDTrainingIntro"
TDTrainingIntroClock = core.Clock()
TrainingBeginTxt = visual.TextStim(win=win, name='TrainingBeginTxt',
    text='We will begin with a training session using a fake speech created by the researchers.\n\nDuring the training, you will see the number of target syllables you recorded and your average response speed. \n\n\n\n\n\nPress SPACE to begin training',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
TrainingContinueKey = keyboard.Keyboard()

# Initialize components for Routine "TrainingSample"
TrainingSampleClock = core.Clock()
SampleMssg2 = visual.TextStim(win=win, name='SampleMssg2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
TrainigTarget = visual.TextStim(win=win, name='TrainigTarget',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
trainingcount = 0
TrainingNumber = visual.TextStim(win=win, name='TrainingNumber',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TrainingSampleContinue = visual.TextStim(win=win, name='TrainingSampleContinue',
    text='Press SPACE to listen to this syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
TSContinueKey = keyboard.Keyboard()

# Initialize components for Routine "TrainingPlaySample"
TrainingPlaySampleClock = core.Clock()
TrainingSampleSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TrainingSampleSound')
TrainingSampleSound.setVolume(0.3)
TraingRepeatSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TraingRepeatSound')
TraingRepeatSound.setVolume(0.3)
TrainTargetTxt = visual.TextStim(win=win, name='TrainTargetTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TrainingBeginSample = visual.TextStim(win=win, name='TrainingBeginSample',
    text='Press SPACE to begin listening',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
TrainingNumber2 = visual.TextStim(win=win, name='TrainingNumber2',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrainEndSample = keyboard.Keyboard()

# Initialize components for Routine "TrainStart"
TrainStartClock = core.Clock()
Three = visual.TextStim(win=win, name='Three',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Two = visual.TextStim(win=win, name='Two',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text = visual.TextStim(win=win, name='text',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "train"
trainClock = core.Clock()
respOnset = 0 
TargetOnset = 0 # Target sound onset
previousOnset = 0 
respcount = 0 # Number of "hits"
TrainRT = 0 # Sum of all RTs

mytimer = core.Clock()
TDTrainSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TDTrainSound')
TDTrainSound.setVolume(0.3)
TrainResp = keyboard.Keyboard()
TDTrainTxt = visual.TextStim(win=win, name='TDTrainTxt',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Cross3 = visual.TextStim(win=win, name='Cross3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Pause1sec"
Pause1secClock = core.Clock()
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "TDTrainFeedback"
TDTrainFeedbackClock = core.Clock()
TDTrainFeedbackMssg = visual.TextStim(win=win, name='TDTrainFeedbackMssg',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EndFeedback = keyboard.Keyboard()
TrainingContinue = visual.TextStim(win=win, name='TrainingContinue',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "P1IntroII"
P1IntroIIClock = core.Clock()
P1Intro2Txt = visual.TextStim(win=win, name='P1Intro2Txt',
    text="Great job! \nLet's now work with the actual speech. Remember to try your best to press SPACE at the same time as the target syllable onset.\nThere will be no feedback given this time. \n\n\nThere are 36 recordings in total. You may take a short break at the beginning of each recording if you wish.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
partone = "0"
parttwo = "0"
partthree = "0"

# Initialize components for Routine "SampleIntro"
SampleIntroClock = core.Clock()
TargetMssg = visual.TextStim(win=win, name='TargetMssg',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PlayTargetKey = keyboard.Keyboard()
TargetTxt = visual.TextStim(win=win, name='TargetTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
repeatCount = 0
TrialNoTxt = visual.TextStim(win=win, name='TrialNoTxt',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ContinueTxt4 = visual.TextStim(win=win, name='ContinueTxt4',
    text='Press SPACE to hear the syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "PlaySample"
PlaySampleClock = core.Clock()
EndPlay = keyboard.Keyboard()
SyllableSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SyllableSound')
SyllableSound.setVolume(1.0)
Repeat = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Repeat')
Repeat.setVolume(1)
SoundTxt = visual.TextStim(win=win, name='SoundTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ContinueKey2 = visual.TextStim(win=win, name='ContinueKey2',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrialNoTxt2 = visual.TextStim(win=win, name='TrialNoTxt2',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "TDStart"
TDStartClock = core.Clock()
Countdown1 = visual.TextStim(win=win, name='Countdown1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_separate"
trial_separateClock = core.Clock()
respOnsetP = 0 
respcountP = 0
previousOnsetP = 0
TargetOnsetP = 0 # Target sound onset
OccurenceC = 1
hit = 0
mytimerP = core.Clock()
PlaySound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PlaySound')
PlaySound.setVolume(1)
PlayText = visual.TextStim(win=win, name='PlayText',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PlayResp = keyboard.Keyboard()
TargetSoundTxt = visual.TextStim(win=win, name='TargetSoundTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Pause1sec"
Pause1secClock = core.Clock()
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AddRespCountCode"
AddRespCountCodeClock = core.Clock()

# Initialize components for Routine "AttentionCheck3"
AttentionCheck3Clock = core.Clock()
AttnCheck3ContKey = keyboard.Keyboard()
AttnCheck3Txt = visual.TextStim(win=win, name='AttnCheck3Txt',
    text='What is your favorite drink?\n\n(Please type your answer in the box below)',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
AttnCheck3Resp = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0, -0.2),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='AttnCheck3Resp',
     autoLog=True,
)
AttnCheck3Cont = visual.TextStim(win=win, name='AttnCheck3Cont',
    text='Press ENTER to submit',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "SampleIntro"
SampleIntroClock = core.Clock()
TargetMssg = visual.TextStim(win=win, name='TargetMssg',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PlayTargetKey = keyboard.Keyboard()
TargetTxt = visual.TextStim(win=win, name='TargetTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
repeatCount = 0
TrialNoTxt = visual.TextStim(win=win, name='TrialNoTxt',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ContinueTxt4 = visual.TextStim(win=win, name='ContinueTxt4',
    text='Press SPACE to hear the syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "PlaySample"
PlaySampleClock = core.Clock()
EndPlay = keyboard.Keyboard()
SyllableSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SyllableSound')
SyllableSound.setVolume(1.0)
Repeat = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Repeat')
Repeat.setVolume(1)
SoundTxt = visual.TextStim(win=win, name='SoundTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ContinueKey2 = visual.TextStim(win=win, name='ContinueKey2',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrialNoTxt2 = visual.TextStim(win=win, name='TrialNoTxt2',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "TDStart"
TDStartClock = core.Clock()
Countdown1 = visual.TextStim(win=win, name='Countdown1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_separate"
trial_separateClock = core.Clock()
respOnsetP = 0 
respcountP = 0
previousOnsetP = 0
TargetOnsetP = 0 # Target sound onset
OccurenceC = 1
hit = 0
mytimerP = core.Clock()
PlaySound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PlaySound')
PlaySound.setVolume(1)
PlayText = visual.TextStim(win=win, name='PlayText',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PlayResp = keyboard.Keyboard()
TargetSoundTxt = visual.TextStim(win=win, name='TargetSoundTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Pause1sec"
Pause1secClock = core.Clock()
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AddRespCountCode"
AddRespCountCodeClock = core.Clock()

# Initialize components for Routine "AttentionCheck1"
AttentionCheck1Clock = core.Clock()
AttentionKey1 = keyboard.Keyboard()
AttentionCheck1Txt = visual.TextStim(win=win, name='AttentionCheck1Txt',
    text='What is your favorite colour?\n\n(Please type your answer in the box below)',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
AttnCheck1Resp = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0, -0.2),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='AttnCheck1Resp',
     autoLog=True,
)
AttnCheck1Cont = visual.TextStim(win=win, name='AttnCheck1Cont',
    text='Press ENTER to submit',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "SampleIntro"
SampleIntroClock = core.Clock()
TargetMssg = visual.TextStim(win=win, name='TargetMssg',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PlayTargetKey = keyboard.Keyboard()
TargetTxt = visual.TextStim(win=win, name='TargetTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
repeatCount = 0
TrialNoTxt = visual.TextStim(win=win, name='TrialNoTxt',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ContinueTxt4 = visual.TextStim(win=win, name='ContinueTxt4',
    text='Press SPACE to hear the syllable',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "PlaySample"
PlaySampleClock = core.Clock()
EndPlay = keyboard.Keyboard()
SyllableSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SyllableSound')
SyllableSound.setVolume(1.0)
Repeat = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Repeat')
Repeat.setVolume(1)
SoundTxt = visual.TextStim(win=win, name='SoundTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ContinueKey2 = visual.TextStim(win=win, name='ContinueKey2',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='The target syllable is:\n\n\n\n\n(Press SPACE when you hear this syllable in the recording)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
TrialNoTxt2 = visual.TextStim(win=win, name='TrialNoTxt2',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "TDStart"
TDStartClock = core.Clock()
Countdown1 = visual.TextStim(win=win, name='Countdown1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_separate"
trial_separateClock = core.Clock()
respOnsetP = 0 
respcountP = 0
previousOnsetP = 0
TargetOnsetP = 0 # Target sound onset
OccurenceC = 1
hit = 0
mytimerP = core.Clock()
PlaySound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PlaySound')
PlaySound.setVolume(1)
PlayText = visual.TextStim(win=win, name='PlayText',
    text='\n\n\n\nPress SPACE as quickly as possible when you hear the target syllable',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
PlayResp = keyboard.Keyboard()
TargetSoundTxt = visual.TextStim(win=win, name='TargetSoundTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Pause1sec"
Pause1secClock = core.Clock()
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AddRespCountCode"
AddRespCountCodeClock = core.Clock()

# Initialize components for Routine "TakeBreak"
TakeBreakClock = core.Clock()
P2IntroTxt = visual.TextStim(win=win, name='P2IntroTxt',
    text='Thank you for your help! You may take a short break now if you wish.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueTxt5 = visual.TextStim(win=win, name='ContinueTxt5',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ContinueKey5 = keyboard.Keyboard()

# Initialize components for Routine "P2Welcome"
P2WelcomeClock = core.Clock()
P2WelcomeTxt = visual.TextStim(win=win, name='P2WelcomeTxt',
    text="It seems like the alien speech contains regularly repeating 'words'. In the next part of this study, you will be asked to distinguish these alien words from other sounds.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
P2WelcomeCont = visual.TextStim(win=win, name='P2WelcomeCont',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
P2WelcomeContKey = keyboard.Keyboard()

# Initialize components for Routine "FamRatingIntro"
FamRatingIntroClock = core.Clock()
FamRateIntroTxt = visual.TextStim(win=win, name='FamRateIntroTxt',
    text='In this part, you will listen to short speech sounds. Some of these may sound familiar to you, as they were spoken in the first part of the study. Others may sound unfamiliar, as they were not spoken in the first part of the study.\n\nYour job is to listen carefully to these short sounds and rate how familiar they sound to you on a scale of 1 (Not familiar) to 4 (Very familiar).\n\nThere will be 12 trials in total.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
FamIntroCont = visual.TextStim(win=win, name='FamIntroCont',
    text='Press SPACE to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
FamRateIntroKey = keyboard.Keyboard()

# Initialize components for Routine "Pause1sec"
Pause1secClock = core.Clock()
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FamRating"
FamRatingClock = core.Clock()
FamRatePrompt = visual.TextStim(win=win, name='FamRatePrompt',
    text='How familiar does this word sound?\n(Press the corresponding number on your keyboard)',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
RatingScale = visual.TextStim(win=win, name='RatingScale',
    text='1 ----------------- 2 ----------------- 3 ----------------- 4',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
RatingScale2 = visual.TextStim(win=win, name='RatingScale2',
    text='\n\n(Not familiar)                                                                     (Very familiar)',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
FamRatingResp = keyboard.Keyboard()
Syllab1 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Syllab1')
Syllab1.setVolume(1)
Syllab2 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Syllab2')
Syllab2.setVolume(1)
Syllab3 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Syllab3')
Syllab3.setVolume(1)

# Initialize components for Routine "AttentionCheck2"
AttentionCheck2Clock = core.Clock()
AttentionKey2 = keyboard.Keyboard()
AttentionCheck2Txt = visual.TextStim(win=win, name='AttentionCheck2Txt',
    text='What is your favorite food?\n\n(Please type your answer in the box below)',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
AttnCheck2Resp = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0, -0.2),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='AttnCheck2Resp',
     autoLog=True,
)
AttnCheck2Cont = visual.TextStim(win=win, name='AttnCheck2Cont',
    text='Press ENTER to submit',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Part2Intro2"
Part2Intro2Clock = core.Clock()
P2IntroTxt2 = visual.TextStim(win=win, name='P2IntroTxt2',
    text='In the next part, you will hear two speech sounds. Your task is to indicate whether the first or the second one sounds like a word from the language you just listened to.\n\nThere will be 16 trials in total.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey6 = visual.TextStim(win=win, name='ContinueKey6',
    text='Press SPACE to begin ',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ContinueKey7 = keyboard.Keyboard()

# Initialize components for Routine "count"
countClock = core.Clock()
AFCcount = 0

# Initialize components for Routine "AFCStart"
AFCStartClock = core.Clock()
QuestionNoTxt = visual.TextStim(win=win, name='QuestionNoTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AFCFirst"
AFCFirstClock = core.Clock()
Word1No = visual.TextStim(win=win, name='Word1No',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Word_1_1 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_1_1')
Word_1_1.setVolume(1)
Word_1_2 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_1_2')
Word_1_2.setVolume(1)
Word_1_3 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_1_3')
Word_1_3.setVolume(1)

# Initialize components for Routine "AFCSecond"
AFCSecondClock = core.Clock()
Word2No = visual.TextStim(win=win, name='Word2No',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Word_2_1 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_2_1')
Word_2_1.setVolume(1)
Word_2_2 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_2_2')
Word_2_2.setVolume(1)
Word_2_3 = sound.Sound('A', secs=0.38, stereo=True, hamming=True,
    name='Word_2_3')
Word_2_3.setVolume(1)

# Initialize components for Routine "AFCQuestion"
AFCQuestionClock = core.Clock()
QuestionTxt = visual.TextStim(win=win, name='QuestionTxt',
    text='Which word sounded correct?\n(Press the corresponding number on your keyboard)',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AFCResp = keyboard.Keyboard()

# Initialize components for Routine "HearingCheckIntro"
HearingCheckIntroClock = core.Clock()
HearingCheckTxt = visual.TextStim(win=win, name='HearingCheckTxt',
    text='Thank you for helping the researchers!\n\nLastly, we will play you a few short speech sounds. In each trial, please select the syllable that matches with the sound you hear.\n\n\n\n\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
EndKey2 = keyboard.Keyboard()

# Initialize components for Routine "Pause1sec"
Pause1secClock = core.Clock()
PauseTxt2 = visual.TextStim(win=win, name='PauseTxt2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "HearingCheck"
HearingCheckClock = core.Clock()
CheckWord = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='CheckWord')
CheckWord.setVolume(1)
WordOptions = visual.TextStim(win=win, name='WordOptions',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CheckQuestion = visual.TextStim(win=win, name='CheckQuestion',
    text='Which sound did you hear?\n(Press the corresponding number on your keyboard)',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
CheckRespKey = keyboard.Keyboard()

# Initialize components for Routine "P2End"
P2EndClock = core.Clock()
EndAllKey = keyboard.Keyboard()
FeedbackQ = visual.TextStim(win=win, name='FeedbackQ',
    text='Please use this section to leave any comment or feedback on the study. (Was there any technical difficulty? Any instruction that was unclear? etc.)',
    font='Times New Roman',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
EndMssg_Ver2 = visual.TextStim(win=win, name='EndMssg_Ver2',
    text='Thank you for completing the tasks! We appreciate your time and cooporation. \n\nYou may now exit the study by pressing ENTER.\nOnce you exit the study, you will be redirected back to prolific where you will receive your completion code.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome0"-------
continueRoutine = True
# update component parameters for each repeat
Welcome0Continue.keys = []
Welcome0Continue.rt = []
_Welcome0Continue_allKeys = []
# keep track of which components have finished
Welcome0Components = [Welcome0Mssg, Welcome0Continue]
for thisComponent in Welcome0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome0Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome0"-------
while continueRoutine:
    # get current time
    t = Welcome0Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome0Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome0Mssg* updates
    if Welcome0Mssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome0Mssg.frameNStart = frameN  # exact frame index
        Welcome0Mssg.tStart = t  # local t and not account for scr refresh
        Welcome0Mssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome0Mssg, 'tStartRefresh')  # time at next scr refresh
        Welcome0Mssg.setAutoDraw(True)
    
    # *Welcome0Continue* updates
    waitOnFlip = False
    if Welcome0Continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome0Continue.frameNStart = frameN  # exact frame index
        Welcome0Continue.tStart = t  # local t and not account for scr refresh
        Welcome0Continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome0Continue, 'tStartRefresh')  # time at next scr refresh
        Welcome0Continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Welcome0Continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Welcome0Continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Welcome0Continue.status == STARTED and not waitOnFlip:
        theseKeys = Welcome0Continue.getKeys(keyList=['space'], waitRelease=False)
        _Welcome0Continue_allKeys.extend(theseKeys)
        if len(_Welcome0Continue_allKeys):
            Welcome0Continue.keys = _Welcome0Continue_allKeys[-1].name  # just the last key pressed
            Welcome0Continue.rt = _Welcome0Continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome0"-------
for thisComponent in Welcome0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome0Mssg.started', Welcome0Mssg.tStartRefresh)
thisExp.addData('Welcome0Mssg.stopped', Welcome0Mssg.tStopRefresh)
# check responses
if Welcome0Continue.keys in ['', [], None]:  # No response was made
    Welcome0Continue.keys = None
thisExp.addData('Welcome0Continue.keys',Welcome0Continue.keys)
if Welcome0Continue.keys != None:  # we had a response
    thisExp.addData('Welcome0Continue.rt', Welcome0Continue.rt)
thisExp.addData('Welcome0Continue.started', Welcome0Continue.tStartRefresh)
thisExp.addData('Welcome0Continue.stopped', Welcome0Continue.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SoundCheckIntro"-------
continueRoutine = True
# update component parameters for each repeat
SoundCheckBegin.keys = []
SoundCheckBegin.rt = []
_SoundCheckBegin_allKeys = []
# keep track of which components have finished
SoundCheckIntroComponents = [SoundCheckTxt, SoundCheckBegin]
for thisComponent in SoundCheckIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SoundCheckIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SoundCheckIntro"-------
while continueRoutine:
    # get current time
    t = SoundCheckIntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SoundCheckIntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *SoundCheckTxt* updates
    if SoundCheckTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SoundCheckTxt.frameNStart = frameN  # exact frame index
        SoundCheckTxt.tStart = t  # local t and not account for scr refresh
        SoundCheckTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SoundCheckTxt, 'tStartRefresh')  # time at next scr refresh
        SoundCheckTxt.setAutoDraw(True)
    
    # *SoundCheckBegin* updates
    waitOnFlip = False
    if SoundCheckBegin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SoundCheckBegin.frameNStart = frameN  # exact frame index
        SoundCheckBegin.tStart = t  # local t and not account for scr refresh
        SoundCheckBegin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SoundCheckBegin, 'tStartRefresh')  # time at next scr refresh
        SoundCheckBegin.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SoundCheckBegin.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SoundCheckBegin.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SoundCheckBegin.status == STARTED and not waitOnFlip:
        theseKeys = SoundCheckBegin.getKeys(keyList=['space'], waitRelease=False)
        _SoundCheckBegin_allKeys.extend(theseKeys)
        if len(_SoundCheckBegin_allKeys):
            SoundCheckBegin.keys = _SoundCheckBegin_allKeys[-1].name  # just the last key pressed
            SoundCheckBegin.rt = _SoundCheckBegin_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SoundCheckIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SoundCheckIntro"-------
for thisComponent in SoundCheckIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SoundCheckTxt.started', SoundCheckTxt.tStartRefresh)
thisExp.addData('SoundCheckTxt.stopped', SoundCheckTxt.tStopRefresh)
# check responses
if SoundCheckBegin.keys in ['', [], None]:  # No response was made
    SoundCheckBegin.keys = None
thisExp.addData('SoundCheckBegin.keys',SoundCheckBegin.keys)
if SoundCheckBegin.keys != None:  # we had a response
    thisExp.addData('SoundCheckBegin.rt', SoundCheckBegin.rt)
thisExp.addData('SoundCheckBegin.started', SoundCheckBegin.tStartRefresh)
thisExp.addData('SoundCheckBegin.stopped', SoundCheckBegin.tStopRefresh)
thisExp.nextEntry()
# the Routine "SoundCheckIntro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SoundCheck"-------
continueRoutine = True
# update component parameters for each repeat
VolumeAdjust.setSound('volumeadjust.wav', hamming=True)
VolumeAdjust.setVolume(0.4, log=False)
SoundCheckEndKey.keys = []
SoundCheckEndKey.rt = []
_SoundCheckEndKey_allKeys = []
# keep track of which components have finished
SoundCheckComponents = [VolumeAdjust, SoundCheckEndTxt, SoundCheckEndKey]
for thisComponent in SoundCheckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SoundCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "SoundCheck"-------
while continueRoutine:
    # get current time
    t = SoundCheckClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SoundCheckClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop VolumeAdjust
    if VolumeAdjust.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VolumeAdjust.frameNStart = frameN  # exact frame index
        VolumeAdjust.tStart = t  # local t and not account for scr refresh
        VolumeAdjust.tStartRefresh = tThisFlipGlobal  # on global time
        VolumeAdjust.play(when=win)  # sync with win flip
    
    # *SoundCheckEndTxt* updates
    if SoundCheckEndTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SoundCheckEndTxt.frameNStart = frameN  # exact frame index
        SoundCheckEndTxt.tStart = t  # local t and not account for scr refresh
        SoundCheckEndTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SoundCheckEndTxt, 'tStartRefresh')  # time at next scr refresh
        SoundCheckEndTxt.setAutoDraw(True)
    
    # *SoundCheckEndKey* updates
    waitOnFlip = False
    if SoundCheckEndKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SoundCheckEndKey.frameNStart = frameN  # exact frame index
        SoundCheckEndKey.tStart = t  # local t and not account for scr refresh
        SoundCheckEndKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SoundCheckEndKey, 'tStartRefresh')  # time at next scr refresh
        SoundCheckEndKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SoundCheckEndKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SoundCheckEndKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SoundCheckEndKey.status == STARTED and not waitOnFlip:
        theseKeys = SoundCheckEndKey.getKeys(keyList=['space'], waitRelease=False)
        _SoundCheckEndKey_allKeys.extend(theseKeys)
        if len(_SoundCheckEndKey_allKeys):
            SoundCheckEndKey.keys = _SoundCheckEndKey_allKeys[-1].name  # just the last key pressed
            SoundCheckEndKey.rt = _SoundCheckEndKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SoundCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SoundCheck"-------
for thisComponent in SoundCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
VolumeAdjust.stop()  # ensure sound has stopped at end of routine
thisExp.addData('VolumeAdjust.started', VolumeAdjust.tStartRefresh)
thisExp.addData('VolumeAdjust.stopped', VolumeAdjust.tStopRefresh)
thisExp.addData('SoundCheckEndTxt.started', SoundCheckEndTxt.tStartRefresh)
thisExp.addData('SoundCheckEndTxt.stopped', SoundCheckEndTxt.tStopRefresh)
# check responses
if SoundCheckEndKey.keys in ['', [], None]:  # No response was made
    SoundCheckEndKey.keys = None
thisExp.addData('SoundCheckEndKey.keys',SoundCheckEndKey.keys)
if SoundCheckEndKey.keys != None:  # we had a response
    thisExp.addData('SoundCheckEndKey.rt', SoundCheckEndKey.rt)
thisExp.addData('SoundCheckEndKey.started', SoundCheckEndKey.tStartRefresh)
thisExp.addData('SoundCheckEndKey.stopped', SoundCheckEndKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "SoundCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "HeadphoneCheck"-------
continueRoutine = True
# update component parameters for each repeat
HeadphoneContinueKey.keys = []
HeadphoneContinueKey.rt = []
_HeadphoneContinueKey_allKeys = []
# keep track of which components have finished
HeadphoneCheckComponents = [HeadphoneCheckTxt, HeadphoneContinue, HeadphoneContinueKey]
for thisComponent in HeadphoneCheckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
HeadphoneCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "HeadphoneCheck"-------
while continueRoutine:
    # get current time
    t = HeadphoneCheckClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=HeadphoneCheckClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *HeadphoneCheckTxt* updates
    if HeadphoneCheckTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HeadphoneCheckTxt.frameNStart = frameN  # exact frame index
        HeadphoneCheckTxt.tStart = t  # local t and not account for scr refresh
        HeadphoneCheckTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HeadphoneCheckTxt, 'tStartRefresh')  # time at next scr refresh
        HeadphoneCheckTxt.setAutoDraw(True)
    
    # *HeadphoneContinue* updates
    if HeadphoneContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HeadphoneContinue.frameNStart = frameN  # exact frame index
        HeadphoneContinue.tStart = t  # local t and not account for scr refresh
        HeadphoneContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HeadphoneContinue, 'tStartRefresh')  # time at next scr refresh
        HeadphoneContinue.setAutoDraw(True)
    
    # *HeadphoneContinueKey* updates
    waitOnFlip = False
    if HeadphoneContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HeadphoneContinueKey.frameNStart = frameN  # exact frame index
        HeadphoneContinueKey.tStart = t  # local t and not account for scr refresh
        HeadphoneContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HeadphoneContinueKey, 'tStartRefresh')  # time at next scr refresh
        HeadphoneContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(HeadphoneContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(HeadphoneContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if HeadphoneContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = HeadphoneContinueKey.getKeys(keyList=['space'], waitRelease=False)
        _HeadphoneContinueKey_allKeys.extend(theseKeys)
        if len(_HeadphoneContinueKey_allKeys):
            HeadphoneContinueKey.keys = _HeadphoneContinueKey_allKeys[-1].name  # just the last key pressed
            HeadphoneContinueKey.rt = _HeadphoneContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HeadphoneCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "HeadphoneCheck"-------
for thisComponent in HeadphoneCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('HeadphoneCheckTxt.started', HeadphoneCheckTxt.tStartRefresh)
thisExp.addData('HeadphoneCheckTxt.stopped', HeadphoneCheckTxt.tStopRefresh)
thisExp.addData('HeadphoneContinue.started', HeadphoneContinue.tStartRefresh)
thisExp.addData('HeadphoneContinue.stopped', HeadphoneContinue.tStopRefresh)
# check responses
if HeadphoneContinueKey.keys in ['', [], None]:  # No response was made
    HeadphoneContinueKey.keys = None
thisExp.addData('HeadphoneContinueKey.keys',HeadphoneContinueKey.keys)
if HeadphoneContinueKey.keys != None:  # we had a response
    thisExp.addData('HeadphoneContinueKey.rt', HeadphoneContinueKey.rt)
thisExp.addData('HeadphoneContinueKey.started', HeadphoneContinueKey.tStartRefresh)
thisExp.addData('HeadphoneContinueKey.stopped', HeadphoneContinueKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "HeadphoneCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
HeadphoneLoop = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Headphone_check.xlsx'),
    seed=None, name='HeadphoneLoop')
thisExp.addLoop(HeadphoneLoop)  # add the loop to the experiment
thisHeadphoneLoop = HeadphoneLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHeadphoneLoop.rgb)
if thisHeadphoneLoop != None:
    for paramName in thisHeadphoneLoop:
        exec('{} = thisHeadphoneLoop[paramName]'.format(paramName))

for thisHeadphoneLoop in HeadphoneLoop:
    currentLoop = HeadphoneLoop
    # abbreviate parameter names if possible (e.g. rgb = thisHeadphoneLoop.rgb)
    if thisHeadphoneLoop != None:
        for paramName in thisHeadphoneLoop:
            exec('{} = thisHeadphoneLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "HeadphonePlay"-------
    continueRoutine = True
    # update component parameters for each repeat
    CheckSound.setSound(File, hamming=True)
    CheckSound.setVolume(1, log=False)
    CheckResp.keys = []
    CheckResp.rt = []
    _CheckResp_allKeys = []
    TrialNumber.setText(checkcount)
    counter += 1
    checkcount = str(counter) + "/6"
    # keep track of which components have finished
    HeadphonePlayComponents = [CheckSound, CheckTxt, CheckResp, TrialNumber, Cross2]
    for thisComponent in HeadphonePlayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HeadphonePlayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HeadphonePlay"-------
    while continueRoutine:
        # get current time
        t = HeadphonePlayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HeadphonePlayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop CheckSound
        if CheckSound.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckSound.frameNStart = frameN  # exact frame index
            CheckSound.tStart = t  # local t and not account for scr refresh
            CheckSound.tStartRefresh = tThisFlipGlobal  # on global time
            CheckSound.play(when=win)  # sync with win flip
        
        # *CheckTxt* updates
        if CheckTxt.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckTxt.frameNStart = frameN  # exact frame index
            CheckTxt.tStart = t  # local t and not account for scr refresh
            CheckTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckTxt, 'tStartRefresh')  # time at next scr refresh
            CheckTxt.setAutoDraw(True)
        
        # *CheckResp* updates
        waitOnFlip = False
        if CheckResp.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckResp.frameNStart = frameN  # exact frame index
            CheckResp.tStart = t  # local t and not account for scr refresh
            CheckResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckResp, 'tStartRefresh')  # time at next scr refresh
            CheckResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CheckResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CheckResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if CheckResp.status == STARTED and not waitOnFlip:
            theseKeys = CheckResp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _CheckResp_allKeys.extend(theseKeys)
            if len(_CheckResp_allKeys):
                CheckResp.keys = _CheckResp_allKeys[-1].name  # just the last key pressed
                CheckResp.rt = _CheckResp_allKeys[-1].rt
                # was this correct?
                if (CheckResp.keys == str(Correct)) or (CheckResp.keys == Correct):
                    CheckResp.corr = 1
                else:
                    CheckResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *TrialNumber* updates
        if TrialNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialNumber.frameNStart = frameN  # exact frame index
            TrialNumber.tStart = t  # local t and not account for scr refresh
            TrialNumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialNumber, 'tStartRefresh')  # time at next scr refresh
            TrialNumber.setAutoDraw(True)
        if TrialNumber.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TrialNumber.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                TrialNumber.tStop = t  # not accounting for scr refresh
                TrialNumber.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TrialNumber, 'tStopRefresh')  # time at next scr refresh
                TrialNumber.setAutoDraw(False)
        
        # *Cross2* updates
        if Cross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross2.frameNStart = frameN  # exact frame index
            Cross2.tStart = t  # local t and not account for scr refresh
            Cross2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross2, 'tStartRefresh')  # time at next scr refresh
            Cross2.setAutoDraw(True)
        if Cross2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross2.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Cross2.tStop = t  # not accounting for scr refresh
                Cross2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross2, 'tStopRefresh')  # time at next scr refresh
                Cross2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphonePlayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HeadphonePlay"-------
    for thisComponent in HeadphonePlayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CheckSound.stop()  # ensure sound has stopped at end of routine
    HeadphoneLoop.addData('CheckSound.started', CheckSound.tStartRefresh)
    HeadphoneLoop.addData('CheckSound.stopped', CheckSound.tStopRefresh)
    HeadphoneLoop.addData('CheckTxt.started', CheckTxt.tStartRefresh)
    HeadphoneLoop.addData('CheckTxt.stopped', CheckTxt.tStopRefresh)
    # check responses
    if CheckResp.keys in ['', [], None]:  # No response was made
        CheckResp.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
           CheckResp.corr = 1;  # correct non-response
        else:
           CheckResp.corr = 0;  # failed to respond (incorrectly)
    # store data for HeadphoneLoop (TrialHandler)
    HeadphoneLoop.addData('CheckResp.keys',CheckResp.keys)
    HeadphoneLoop.addData('CheckResp.corr', CheckResp.corr)
    if CheckResp.keys != None:  # we had a response
        HeadphoneLoop.addData('CheckResp.rt', CheckResp.rt)
    HeadphoneLoop.addData('CheckResp.started', CheckResp.tStartRefresh)
    HeadphoneLoop.addData('CheckResp.stopped', CheckResp.tStopRefresh)
    HeadphoneLoop.addData('TrialNumber.started', TrialNumber.tStartRefresh)
    HeadphoneLoop.addData('TrialNumber.stopped', TrialNumber.tStopRefresh)
    if CheckResp.corr == 1:
        message = "CORRECT"
    else:
        message = "INCORRECT"
    HeadphoneLoop.addData('Cross2.started', Cross2.tStartRefresh)
    HeadphoneLoop.addData('Cross2.stopped', Cross2.tStopRefresh)
    # the Routine "HeadphonePlay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "HeadphoneFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    FeedbackMssg.setText(message)
    # keep track of which components have finished
    HeadphoneFeedbackComponents = [FeedbackMssg]
    for thisComponent in HeadphoneFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HeadphoneFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HeadphoneFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = HeadphoneFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HeadphoneFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FeedbackMssg* updates
        if FeedbackMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FeedbackMssg.frameNStart = frameN  # exact frame index
            FeedbackMssg.tStart = t  # local t and not account for scr refresh
            FeedbackMssg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FeedbackMssg, 'tStartRefresh')  # time at next scr refresh
            FeedbackMssg.setAutoDraw(True)
        if FeedbackMssg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FeedbackMssg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FeedbackMssg.tStop = t  # not accounting for scr refresh
                FeedbackMssg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FeedbackMssg, 'tStopRefresh')  # time at next scr refresh
                FeedbackMssg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphoneFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HeadphoneFeedback"-------
    for thisComponent in HeadphoneFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    HeadphoneLoop.addData('FeedbackMssg.started', FeedbackMssg.tStartRefresh)
    HeadphoneLoop.addData('FeedbackMssg.stopped', FeedbackMssg.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'HeadphoneLoop'


# set up handler to look after randomisation of conditions etc
Randomization = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Counterbalance.xlsx'),
    seed=None, name='Randomization')
thisExp.addLoop(Randomization)  # add the loop to the experiment
thisRandomization = Randomization.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRandomization.rgb)
if thisRandomization != None:
    for paramName in thisRandomization:
        exec('{} = thisRandomization[paramName]'.format(paramName))

for thisRandomization in Randomization:
    currentLoop = Randomization
    # abbreviate parameter names if possible (e.g. rgb = thisRandomization.rgb)
    if thisRandomization != None:
        for paramName in thisRandomization:
            exec('{} = thisRandomization[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    MSTLoop = data.TrialHandler(nReps=WordOrder, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='MSTLoop')
    thisExp.addLoop(MSTLoop)  # add the loop to the experiment
    thisMSTLoop = MSTLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMSTLoop.rgb)
    if thisMSTLoop != None:
        for paramName in thisMSTLoop:
            exec('{} = thisMSTLoop[paramName]'.format(paramName))
    
    for thisMSTLoop in MSTLoop:
        currentLoop = MSTLoop
        # abbreviate parameter names if possible (e.g. rgb = thisMSTLoop.rgb)
        if thisMSTLoop != None:
            for paramName in thisMSTLoop:
                exec('{} = thisMSTLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "MSTWelcome"-------
        continueRoutine = True
        # update component parameters for each repeat
        ContinueKey8.keys = []
        ContinueKey8.rt = []
        _ContinueKey8_allKeys = []
        # keep track of which components have finished
        MSTWelcomeComponents = [MSTWelcomeTxt, WelcomeP2Continue, ContinueKey8]
        for thisComponent in MSTWelcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MSTWelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MSTWelcome"-------
        while continueRoutine:
            # get current time
            t = MSTWelcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MSTWelcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MSTWelcomeTxt* updates
            if MSTWelcomeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTWelcomeTxt.frameNStart = frameN  # exact frame index
                MSTWelcomeTxt.tStart = t  # local t and not account for scr refresh
                MSTWelcomeTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTWelcomeTxt, 'tStartRefresh')  # time at next scr refresh
                MSTWelcomeTxt.setAutoDraw(True)
            
            # *WelcomeP2Continue* updates
            if WelcomeP2Continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WelcomeP2Continue.frameNStart = frameN  # exact frame index
                WelcomeP2Continue.tStart = t  # local t and not account for scr refresh
                WelcomeP2Continue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WelcomeP2Continue, 'tStartRefresh')  # time at next scr refresh
                WelcomeP2Continue.setAutoDraw(True)
            
            # *ContinueKey8* updates
            waitOnFlip = False
            if ContinueKey8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey8.frameNStart = frameN  # exact frame index
                ContinueKey8.tStart = t  # local t and not account for scr refresh
                ContinueKey8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey8, 'tStartRefresh')  # time at next scr refresh
                ContinueKey8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ContinueKey8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ContinueKey8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ContinueKey8.status == STARTED and not waitOnFlip:
                theseKeys = ContinueKey8.getKeys(keyList=['space'], waitRelease=False)
                _ContinueKey8_allKeys.extend(theseKeys)
                if len(_ContinueKey8_allKeys):
                    ContinueKey8.keys = _ContinueKey8_allKeys[-1].name  # just the last key pressed
                    ContinueKey8.rt = _ContinueKey8_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MSTWelcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MSTWelcome"-------
        for thisComponent in MSTWelcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MSTLoop.addData('MSTWelcomeTxt.started', MSTWelcomeTxt.tStartRefresh)
        MSTLoop.addData('MSTWelcomeTxt.stopped', MSTWelcomeTxt.tStopRefresh)
        MSTLoop.addData('WelcomeP2Continue.started', WelcomeP2Continue.tStartRefresh)
        MSTLoop.addData('WelcomeP2Continue.stopped', WelcomeP2Continue.tStopRefresh)
        # check responses
        if ContinueKey8.keys in ['', [], None]:  # No response was made
            ContinueKey8.keys = None
        MSTLoop.addData('ContinueKey8.keys',ContinueKey8.keys)
        if ContinueKey8.keys != None:  # we had a response
            MSTLoop.addData('ContinueKey8.rt', ContinueKey8.rt)
        MSTLoop.addData('ContinueKey8.started', ContinueKey8.tStartRefresh)
        MSTLoop.addData('ContinueKey8.stopped', ContinueKey8.tStopRefresh)
        # the Routine "MSTWelcome" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "MSTWelcome2"-------
        continueRoutine = True
        # update component parameters for each repeat
        MSTWelcomeContKey.keys = []
        MSTWelcomeContKey.rt = []
        _MSTWelcomeContKey_allKeys = []
        # keep track of which components have finished
        MSTWelcome2Components = [MSTWelcome2Txt, MSTWelcomeCont, MSTWelcomeContKey]
        for thisComponent in MSTWelcome2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MSTWelcome2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MSTWelcome2"-------
        while continueRoutine:
            # get current time
            t = MSTWelcome2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MSTWelcome2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MSTWelcome2Txt* updates
            if MSTWelcome2Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTWelcome2Txt.frameNStart = frameN  # exact frame index
                MSTWelcome2Txt.tStart = t  # local t and not account for scr refresh
                MSTWelcome2Txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTWelcome2Txt, 'tStartRefresh')  # time at next scr refresh
                MSTWelcome2Txt.setAutoDraw(True)
            
            # *MSTWelcomeCont* updates
            if MSTWelcomeCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTWelcomeCont.frameNStart = frameN  # exact frame index
                MSTWelcomeCont.tStart = t  # local t and not account for scr refresh
                MSTWelcomeCont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTWelcomeCont, 'tStartRefresh')  # time at next scr refresh
                MSTWelcomeCont.setAutoDraw(True)
            
            # *MSTWelcomeContKey* updates
            waitOnFlip = False
            if MSTWelcomeContKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTWelcomeContKey.frameNStart = frameN  # exact frame index
                MSTWelcomeContKey.tStart = t  # local t and not account for scr refresh
                MSTWelcomeContKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTWelcomeContKey, 'tStartRefresh')  # time at next scr refresh
                MSTWelcomeContKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(MSTWelcomeContKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(MSTWelcomeContKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if MSTWelcomeContKey.status == STARTED and not waitOnFlip:
                theseKeys = MSTWelcomeContKey.getKeys(keyList=['space'], waitRelease=False)
                _MSTWelcomeContKey_allKeys.extend(theseKeys)
                if len(_MSTWelcomeContKey_allKeys):
                    MSTWelcomeContKey.keys = _MSTWelcomeContKey_allKeys[-1].name  # just the last key pressed
                    MSTWelcomeContKey.rt = _MSTWelcomeContKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MSTWelcome2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MSTWelcome2"-------
        for thisComponent in MSTWelcome2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MSTLoop.addData('MSTWelcome2Txt.started', MSTWelcome2Txt.tStartRefresh)
        MSTLoop.addData('MSTWelcome2Txt.stopped', MSTWelcome2Txt.tStopRefresh)
        MSTLoop.addData('MSTWelcomeCont.started', MSTWelcomeCont.tStartRefresh)
        MSTLoop.addData('MSTWelcomeCont.stopped', MSTWelcomeCont.tStopRefresh)
        # check responses
        if MSTWelcomeContKey.keys in ['', [], None]:  # No response was made
            MSTWelcomeContKey.keys = None
        MSTLoop.addData('MSTWelcomeContKey.keys',MSTWelcomeContKey.keys)
        if MSTWelcomeContKey.keys != None:  # we had a response
            MSTLoop.addData('MSTWelcomeContKey.rt', MSTWelcomeContKey.rt)
        MSTLoop.addData('MSTWelcomeContKey.started', MSTWelcomeContKey.tStartRefresh)
        MSTLoop.addData('MSTWelcomeContKey.stopped', MSTWelcomeContKey.tStopRefresh)
        # the Routine "MSTWelcome2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "MSTTrainIntro"-------
        continueRoutine = True
        # update component parameters for each repeat
        MSTTrainIntroKey.keys = []
        MSTTrainIntroKey.rt = []
        _MSTTrainIntroKey_allKeys = []
        Randomization.addData('1', Condition)
        
        # keep track of which components have finished
        MSTTrainIntroComponents = [MSTTrainIntroTxt, MSTTrainIntroCont, MSTTrainIntroKey]
        for thisComponent in MSTTrainIntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MSTTrainIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MSTTrainIntro"-------
        while continueRoutine:
            # get current time
            t = MSTTrainIntroClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MSTTrainIntroClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MSTTrainIntroTxt* updates
            if MSTTrainIntroTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTTrainIntroTxt.frameNStart = frameN  # exact frame index
                MSTTrainIntroTxt.tStart = t  # local t and not account for scr refresh
                MSTTrainIntroTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTTrainIntroTxt, 'tStartRefresh')  # time at next scr refresh
                MSTTrainIntroTxt.setAutoDraw(True)
            
            # *MSTTrainIntroCont* updates
            if MSTTrainIntroCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTTrainIntroCont.frameNStart = frameN  # exact frame index
                MSTTrainIntroCont.tStart = t  # local t and not account for scr refresh
                MSTTrainIntroCont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTTrainIntroCont, 'tStartRefresh')  # time at next scr refresh
                MSTTrainIntroCont.setAutoDraw(True)
            
            # *MSTTrainIntroKey* updates
            waitOnFlip = False
            if MSTTrainIntroKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTTrainIntroKey.frameNStart = frameN  # exact frame index
                MSTTrainIntroKey.tStart = t  # local t and not account for scr refresh
                MSTTrainIntroKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTTrainIntroKey, 'tStartRefresh')  # time at next scr refresh
                MSTTrainIntroKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(MSTTrainIntroKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(MSTTrainIntroKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if MSTTrainIntroKey.status == STARTED and not waitOnFlip:
                theseKeys = MSTTrainIntroKey.getKeys(keyList=['space'], waitRelease=False)
                _MSTTrainIntroKey_allKeys.extend(theseKeys)
                if len(_MSTTrainIntroKey_allKeys):
                    MSTTrainIntroKey.keys = _MSTTrainIntroKey_allKeys[-1].name  # just the last key pressed
                    MSTTrainIntroKey.rt = _MSTTrainIntroKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MSTTrainIntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MSTTrainIntro"-------
        for thisComponent in MSTTrainIntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MSTLoop.addData('MSTTrainIntroTxt.started', MSTTrainIntroTxt.tStartRefresh)
        MSTLoop.addData('MSTTrainIntroTxt.stopped', MSTTrainIntroTxt.tStopRefresh)
        MSTLoop.addData('MSTTrainIntroCont.started', MSTTrainIntroCont.tStartRefresh)
        MSTLoop.addData('MSTTrainIntroCont.stopped', MSTTrainIntroCont.tStopRefresh)
        # check responses
        if MSTTrainIntroKey.keys in ['', [], None]:  # No response was made
            MSTTrainIntroKey.keys = None
        MSTLoop.addData('MSTTrainIntroKey.keys',MSTTrainIntroKey.keys)
        if MSTTrainIntroKey.keys != None:  # we had a response
            MSTLoop.addData('MSTTrainIntroKey.rt', MSTTrainIntroKey.rt)
        MSTLoop.addData('MSTTrainIntroKey.started', MSTTrainIntroKey.tStartRefresh)
        MSTLoop.addData('MSTTrainIntroKey.stopped', MSTTrainIntroKey.tStopRefresh)
        # the Routine "MSTTrainIntro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        MSTTrainLoop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('trainSound.xlsx'),
            seed=None, name='MSTTrainLoop')
        thisExp.addLoop(MSTTrainLoop)  # add the loop to the experiment
        thisMSTTrainLoop = MSTTrainLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMSTTrainLoop.rgb)
        if thisMSTTrainLoop != None:
            for paramName in thisMSTTrainLoop:
                exec('{} = thisMSTTrainLoop[paramName]'.format(paramName))
        
        for thisMSTTrainLoop in MSTTrainLoop:
            currentLoop = MSTTrainLoop
            # abbreviate parameter names if possible (e.g. rgb = thisMSTTrainLoop.rgb)
            if thisMSTTrainLoop != None:
                for paramName in thisMSTTrainLoop:
                    exec('{} = thisMSTTrainLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Pause1sec"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Pause1secComponents = [PauseTxt2]
            for thisComponent in Pause1secComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Pause1secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Pause1sec"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Pause1secClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Pause1secClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PauseTxt2* updates
                if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PauseTxt2.frameNStart = frameN  # exact frame index
                    PauseTxt2.tStart = t  # local t and not account for scr refresh
                    PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                    PauseTxt2.setAutoDraw(True)
                if PauseTxt2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        PauseTxt2.tStop = t  # not accounting for scr refresh
                        PauseTxt2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(PauseTxt2, 'tStopRefresh')  # time at next scr refresh
                        PauseTxt2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Pause1secComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Pause1sec"-------
            for thisComponent in Pause1secComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            MSTTrainLoop.addData('PauseTxt2.started', PauseTxt2.tStartRefresh)
            MSTTrainLoop.addData('PauseTxt2.stopped', PauseTxt2.tStopRefresh)
            
            # ------Prepare to start Routine "MSTTrain"-------
            continueRoutine = True
            # update component parameters for each repeat
            MSTTrainSound.setSound(SoundFile, hamming=True)
            MSTTrainSound.setVolume(1, log=False)
            MSTTrainTrialNum.setText(MSTTrialCount)
            # keep track of which components have finished
            MSTTrainComponents = [MSTTrainSound, MSTTrainCross, MSTTrainTrialNum]
            for thisComponent in MSTTrainComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            MSTTrainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "MSTTrain"-------
            while continueRoutine:
                # get current time
                t = MSTTrainClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=MSTTrainClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop MSTTrainSound
                if MSTTrainSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainSound.frameNStart = frameN  # exact frame index
                    MSTTrainSound.tStart = t  # local t and not account for scr refresh
                    MSTTrainSound.tStartRefresh = tThisFlipGlobal  # on global time
                    MSTTrainSound.play(when=win)  # sync with win flip
                
                # *MSTTrainCross* updates
                if MSTTrainCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainCross.frameNStart = frameN  # exact frame index
                    MSTTrainCross.tStart = t  # local t and not account for scr refresh
                    MSTTrainCross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTrainCross, 'tStartRefresh')  # time at next scr refresh
                    MSTTrainCross.setAutoDraw(True)
                if MSTTrainCross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > MSTTrainCross.tStartRefresh + MSTTrainSound.getDuration()-frameTolerance:
                        # keep track of stop time/frame for later
                        MSTTrainCross.tStop = t  # not accounting for scr refresh
                        MSTTrainCross.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(MSTTrainCross, 'tStopRefresh')  # time at next scr refresh
                        MSTTrainCross.setAutoDraw(False)
                
                # *MSTTrainTrialNum* updates
                if MSTTrainTrialNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainTrialNum.frameNStart = frameN  # exact frame index
                    MSTTrainTrialNum.tStart = t  # local t and not account for scr refresh
                    MSTTrainTrialNum.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTrainTrialNum, 'tStartRefresh')  # time at next scr refresh
                    MSTTrainTrialNum.setAutoDraw(True)
                if MSTTrainTrialNum.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > MSTTrainTrialNum.tStartRefresh + MSTTrainSound.getDuration()-frameTolerance:
                        # keep track of stop time/frame for later
                        MSTTrainTrialNum.tStop = t  # not accounting for scr refresh
                        MSTTrainTrialNum.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(MSTTrainTrialNum, 'tStopRefresh')  # time at next scr refresh
                        MSTTrainTrialNum.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MSTTrainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "MSTTrain"-------
            for thisComponent in MSTTrainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #if ResponsePractice.corr == 1:
            #    feedback = "CORRECT"
            #    txtcolor = "lightgreen"
            #else:
            #    feedback = "INCORRECT"
            #    txtcolor = "red"
            #    
            #message = "This is a " + Type + " word."
            Tcount += 1
            MSTTrialCount = 'Trial ' + str(Tcount)
            MSTTrainSound.stop()  # ensure sound has stopped at end of routine
            MSTTrainLoop.addData('MSTTrainSound.started', MSTTrainSound.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainSound.stopped', MSTTrainSound.tStopRefresh)
            MSTTrainLoop.addData('MSTTrainCross.started', MSTTrainCross.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainCross.stopped', MSTTrainCross.tStopRefresh)
            MSTTrainLoop.addData('MSTTrainTrialNum.started', MSTTrainTrialNum.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainTrialNum.stopped', MSTTrainTrialNum.tStopRefresh)
            # the Routine "MSTTrain" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "MSTTrainFeedback"-------
            continueRoutine = True
            # update component parameters for each repeat
            if Type == 'NEW':
                message = "This is a NEW word. \nThis is your first time hearing this word."
            elif Type == 'SIMILAR':
                message = "This is a NEW word. \nNote that this one sounds similar to the previous word but is not exactly the same."
            elif Type == 'OLD':
                message = "This is an OLD word. \nThis word is exactly the same as the first word."
            MSTTrainMssg.setText(message)
            MSTTrainKeys.keys = []
            MSTTrainKeys.rt = []
            _MSTTrainKeys_allKeys = []
            # keep track of which components have finished
            MSTTrainFeedbackComponents = [MSTTrainOptions, MSTTrainMssg, MSTTrainContinueMssg, MSTTrainKeys, MSTTrainCross2]
            for thisComponent in MSTTrainFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            MSTTrainFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "MSTTrainFeedback"-------
            while continueRoutine:
                # get current time
                t = MSTTrainFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=MSTTrainFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *MSTTrainOptions* updates
                if MSTTrainOptions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainOptions.frameNStart = frameN  # exact frame index
                    MSTTrainOptions.tStart = t  # local t and not account for scr refresh
                    MSTTrainOptions.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTrainOptions, 'tStartRefresh')  # time at next scr refresh
                    MSTTrainOptions.setAutoDraw(True)
                
                # *MSTTrainMssg* updates
                if MSTTrainMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainMssg.frameNStart = frameN  # exact frame index
                    MSTTrainMssg.tStart = t  # local t and not account for scr refresh
                    MSTTrainMssg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTrainMssg, 'tStartRefresh')  # time at next scr refresh
                    MSTTrainMssg.setAutoDraw(True)
                
                # *MSTTrainContinueMssg* updates
                if MSTTrainContinueMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainContinueMssg.frameNStart = frameN  # exact frame index
                    MSTTrainContinueMssg.tStart = t  # local t and not account for scr refresh
                    MSTTrainContinueMssg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTrainContinueMssg, 'tStartRefresh')  # time at next scr refresh
                    MSTTrainContinueMssg.setAutoDraw(True)
                
                # *MSTTrainKeys* updates
                waitOnFlip = False
                if MSTTrainKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainKeys.frameNStart = frameN  # exact frame index
                    MSTTrainKeys.tStart = t  # local t and not account for scr refresh
                    MSTTrainKeys.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTrainKeys, 'tStartRefresh')  # time at next scr refresh
                    MSTTrainKeys.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(MSTTrainKeys.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(MSTTrainKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if MSTTrainKeys.status == STARTED and not waitOnFlip:
                    theseKeys = MSTTrainKeys.getKeys(keyList=['1', '2'], waitRelease=False)
                    _MSTTrainKeys_allKeys.extend(theseKeys)
                    if len(_MSTTrainKeys_allKeys):
                        MSTTrainKeys.keys = _MSTTrainKeys_allKeys[-1].name  # just the last key pressed
                        MSTTrainKeys.rt = _MSTTrainKeys_allKeys[-1].rt
                        # was this correct?
                        if (MSTTrainKeys.keys == str(Correct)) or (MSTTrainKeys.keys == Correct):
                            MSTTrainKeys.corr = 1
                        else:
                            MSTTrainKeys.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *MSTTrainCross2* updates
                if MSTTrainCross2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTrainCross2.frameNStart = frameN  # exact frame index
                    MSTTrainCross2.tStart = t  # local t and not account for scr refresh
                    MSTTrainCross2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTrainCross2, 'tStartRefresh')  # time at next scr refresh
                    MSTTrainCross2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MSTTrainFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "MSTTrainFeedback"-------
            for thisComponent in MSTTrainFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            if MSTTrainKeys.corr == 1:
                feedback = 'CORRECT'
            else:
                feedback = 'INCORRECT'
            MSTTrainLoop.addData('MSTTrainOptions.started', MSTTrainOptions.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainOptions.stopped', MSTTrainOptions.tStopRefresh)
            MSTTrainLoop.addData('MSTTrainMssg.started', MSTTrainMssg.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainMssg.stopped', MSTTrainMssg.tStopRefresh)
            MSTTrainLoop.addData('MSTTrainContinueMssg.started', MSTTrainContinueMssg.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainContinueMssg.stopped', MSTTrainContinueMssg.tStopRefresh)
            # check responses
            if MSTTrainKeys.keys in ['', [], None]:  # No response was made
                MSTTrainKeys.keys = None
                # was no response the correct answer?!
                if str(Correct).lower() == 'none':
                   MSTTrainKeys.corr = 1;  # correct non-response
                else:
                   MSTTrainKeys.corr = 0;  # failed to respond (incorrectly)
            # store data for MSTTrainLoop (TrialHandler)
            MSTTrainLoop.addData('MSTTrainKeys.keys',MSTTrainKeys.keys)
            MSTTrainLoop.addData('MSTTrainKeys.corr', MSTTrainKeys.corr)
            if MSTTrainKeys.keys != None:  # we had a response
                MSTTrainLoop.addData('MSTTrainKeys.rt', MSTTrainKeys.rt)
            MSTTrainLoop.addData('MSTTrainKeys.started', MSTTrainKeys.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainKeys.stopped', MSTTrainKeys.tStopRefresh)
            MSTTrainLoop.addData('MSTTrainCross2.started', MSTTrainCross2.tStartRefresh)
            MSTTrainLoop.addData('MSTTrainCross2.stopped', MSTTrainCross2.tStopRefresh)
            # the Routine "MSTTrainFeedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'MSTTrainLoop'
        
        
        # ------Prepare to start Routine "MSTTestStartInstrct"-------
        continueRoutine = True
        # update component parameters for each repeat
        MSTTestBeginKey.keys = []
        MSTTestBeginKey.rt = []
        _MSTTestBeginKey_allKeys = []
        # keep track of which components have finished
        MSTTestStartInstrctComponents = [MSTTestBeginTxt, MSTTestBeginKey, MSTTestBegin]
        for thisComponent in MSTTestStartInstrctComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        MSTTestStartInstrctClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "MSTTestStartInstrct"-------
        while continueRoutine:
            # get current time
            t = MSTTestStartInstrctClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=MSTTestStartInstrctClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MSTTestBeginTxt* updates
            if MSTTestBeginTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTTestBeginTxt.frameNStart = frameN  # exact frame index
                MSTTestBeginTxt.tStart = t  # local t and not account for scr refresh
                MSTTestBeginTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTTestBeginTxt, 'tStartRefresh')  # time at next scr refresh
                MSTTestBeginTxt.setAutoDraw(True)
            
            # *MSTTestBeginKey* updates
            waitOnFlip = False
            if MSTTestBeginKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTTestBeginKey.frameNStart = frameN  # exact frame index
                MSTTestBeginKey.tStart = t  # local t and not account for scr refresh
                MSTTestBeginKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTTestBeginKey, 'tStartRefresh')  # time at next scr refresh
                MSTTestBeginKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(MSTTestBeginKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(MSTTestBeginKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if MSTTestBeginKey.status == STARTED and not waitOnFlip:
                theseKeys = MSTTestBeginKey.getKeys(keyList=['space'], waitRelease=False)
                _MSTTestBeginKey_allKeys.extend(theseKeys)
                if len(_MSTTestBeginKey_allKeys):
                    MSTTestBeginKey.keys = _MSTTestBeginKey_allKeys[-1].name  # just the last key pressed
                    MSTTestBeginKey.rt = _MSTTestBeginKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *MSTTestBegin* updates
            if MSTTestBegin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                MSTTestBegin.frameNStart = frameN  # exact frame index
                MSTTestBegin.tStart = t  # local t and not account for scr refresh
                MSTTestBegin.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(MSTTestBegin, 'tStartRefresh')  # time at next scr refresh
                MSTTestBegin.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MSTTestStartInstrctComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "MSTTestStartInstrct"-------
        for thisComponent in MSTTestStartInstrctComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MSTLoop.addData('MSTTestBeginTxt.started', MSTTestBeginTxt.tStartRefresh)
        MSTLoop.addData('MSTTestBeginTxt.stopped', MSTTestBeginTxt.tStopRefresh)
        # check responses
        if MSTTestBeginKey.keys in ['', [], None]:  # No response was made
            MSTTestBeginKey.keys = None
        MSTLoop.addData('MSTTestBeginKey.keys',MSTTestBeginKey.keys)
        if MSTTestBeginKey.keys != None:  # we had a response
            MSTLoop.addData('MSTTestBeginKey.rt', MSTTestBeginKey.rt)
        MSTLoop.addData('MSTTestBeginKey.started', MSTTestBeginKey.tStartRefresh)
        MSTLoop.addData('MSTTestBeginKey.stopped', MSTTestBeginKey.tStopRefresh)
        MSTLoop.addData('MSTTestBegin.started', MSTTestBegin.tStartRefresh)
        MSTLoop.addData('MSTTestBegin.stopped', MSTTestBegin.tStopRefresh)
        condition = "0:100"
        import random
        c = random.randint(0, 6)
        if c == 0:
            condition = "0:100"
        elif c == 1:
            condition = "100:200"
        elif c == 2:
            condition = "200:300"
        elif c == 3:
            condition = "300:400"
        elif c == 4:
            condition = "400:500"
        elif c == 5:
            condition = "500:600"
        # the Routine "MSTTestStartInstrct" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        MSTPlayLoop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('testSound.xlsx', selection=condition),
            seed=None, name='MSTPlayLoop')
        thisExp.addLoop(MSTPlayLoop)  # add the loop to the experiment
        thisMSTPlayLoop = MSTPlayLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMSTPlayLoop.rgb)
        if thisMSTPlayLoop != None:
            for paramName in thisMSTPlayLoop:
                exec('{} = thisMSTPlayLoop[paramName]'.format(paramName))
        
        for thisMSTPlayLoop in MSTPlayLoop:
            currentLoop = MSTPlayLoop
            # abbreviate parameter names if possible (e.g. rgb = thisMSTPlayLoop.rgb)
            if thisMSTPlayLoop != None:
                for paramName in thisMSTPlayLoop:
                    exec('{} = thisMSTPlayLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "MSTTrialCount"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            MSTcount += 1
            number = str(MSTcount) + "/100"
            # keep track of which components have finished
            MSTTrialCountComponents = [Cross1500ms]
            for thisComponent in MSTTrialCountComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            MSTTrialCountClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "MSTTrialCount"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = MSTTrialCountClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=MSTTrialCountClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Cross1500ms* updates
                if Cross1500ms.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Cross1500ms.frameNStart = frameN  # exact frame index
                    Cross1500ms.tStart = t  # local t and not account for scr refresh
                    Cross1500ms.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Cross1500ms, 'tStartRefresh')  # time at next scr refresh
                    Cross1500ms.setAutoDraw(True)
                if Cross1500ms.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Cross1500ms.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        Cross1500ms.tStop = t  # not accounting for scr refresh
                        Cross1500ms.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Cross1500ms, 'tStopRefresh')  # time at next scr refresh
                        Cross1500ms.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MSTTrialCountComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "MSTTrialCount"-------
            for thisComponent in MSTTrialCountComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            MSTPlayLoop.addData('Cross1500ms.started', Cross1500ms.tStartRefresh)
            MSTPlayLoop.addData('Cross1500ms.stopped', Cross1500ms.tStopRefresh)
            
            # ------Prepare to start Routine "MSTplay"-------
            continueRoutine = True
            # update component parameters for each repeat
            MSTTestPlay.setSound(File, hamming=True)
            MSTTestPlay.setVolume(1, log=False)
            MSTTestOptionKeys.keys = []
            MSTTestOptionKeys.rt = []
            _MSTTestOptionKeys_allKeys = []
            MSTTestTrialNum.setText(number)
            # keep track of which components have finished
            MSTplayComponents = [MSTTestOptions, MSTTestPlay, MSTTestOptionKeys, MSTTestTrialNum, MSTTestNote]
            for thisComponent in MSTplayComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            MSTplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "MSTplay"-------
            while continueRoutine:
                # get current time
                t = MSTplayClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=MSTplayClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *MSTTestOptions* updates
                if MSTTestOptions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTestOptions.frameNStart = frameN  # exact frame index
                    MSTTestOptions.tStart = t  # local t and not account for scr refresh
                    MSTTestOptions.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTestOptions, 'tStartRefresh')  # time at next scr refresh
                    MSTTestOptions.setAutoDraw(True)
                # start/stop MSTTestPlay
                if MSTTestPlay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTestPlay.frameNStart = frameN  # exact frame index
                    MSTTestPlay.tStart = t  # local t and not account for scr refresh
                    MSTTestPlay.tStartRefresh = tThisFlipGlobal  # on global time
                    MSTTestPlay.play(when=win)  # sync with win flip
                
                # *MSTTestOptionKeys* updates
                waitOnFlip = False
                if MSTTestOptionKeys.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTestOptionKeys.frameNStart = frameN  # exact frame index
                    MSTTestOptionKeys.tStart = t  # local t and not account for scr refresh
                    MSTTestOptionKeys.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTestOptionKeys, 'tStartRefresh')  # time at next scr refresh
                    MSTTestOptionKeys.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(MSTTestOptionKeys.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(MSTTestOptionKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if MSTTestOptionKeys.status == STARTED and not waitOnFlip:
                    theseKeys = MSTTestOptionKeys.getKeys(keyList=['1', '2'], waitRelease=False)
                    _MSTTestOptionKeys_allKeys.extend(theseKeys)
                    if len(_MSTTestOptionKeys_allKeys):
                        MSTTestOptionKeys.keys = _MSTTestOptionKeys_allKeys[-1].name  # just the last key pressed
                        MSTTestOptionKeys.rt = _MSTTestOptionKeys_allKeys[-1].rt
                        # was this correct?
                        if (MSTTestOptionKeys.keys == str(Correct)) or (MSTTestOptionKeys.keys == Correct):
                            MSTTestOptionKeys.corr = 1
                        else:
                            MSTTestOptionKeys.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *MSTTestTrialNum* updates
                if MSTTestTrialNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTestTrialNum.frameNStart = frameN  # exact frame index
                    MSTTestTrialNum.tStart = t  # local t and not account for scr refresh
                    MSTTestTrialNum.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTestTrialNum, 'tStartRefresh')  # time at next scr refresh
                    MSTTestTrialNum.setAutoDraw(True)
                
                # *MSTTestNote* updates
                if MSTTestNote.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    MSTTestNote.frameNStart = frameN  # exact frame index
                    MSTTestNote.tStart = t  # local t and not account for scr refresh
                    MSTTestNote.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(MSTTestNote, 'tStartRefresh')  # time at next scr refresh
                    MSTTestNote.setAutoDraw(True)
                if MSTTestNote.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > MSTTestNote.tStartRefresh + 0-frameTolerance:
                        # keep track of stop time/frame for later
                        MSTTestNote.tStop = t  # not accounting for scr refresh
                        MSTTestNote.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(MSTTestNote, 'tStopRefresh')  # time at next scr refresh
                        MSTTestNote.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in MSTplayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "MSTplay"-------
            for thisComponent in MSTplayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            MSTPlayLoop.addData('MSTTestOptions.started', MSTTestOptions.tStartRefresh)
            MSTPlayLoop.addData('MSTTestOptions.stopped', MSTTestOptions.tStopRefresh)
            MSTTestPlay.stop()  # ensure sound has stopped at end of routine
            MSTPlayLoop.addData('MSTTestPlay.started', MSTTestPlay.tStartRefresh)
            MSTPlayLoop.addData('MSTTestPlay.stopped', MSTTestPlay.tStopRefresh)
            # check responses
            if MSTTestOptionKeys.keys in ['', [], None]:  # No response was made
                MSTTestOptionKeys.keys = None
                # was no response the correct answer?!
                if str(Correct).lower() == 'none':
                   MSTTestOptionKeys.corr = 1;  # correct non-response
                else:
                   MSTTestOptionKeys.corr = 0;  # failed to respond (incorrectly)
            # store data for MSTPlayLoop (TrialHandler)
            MSTPlayLoop.addData('MSTTestOptionKeys.keys',MSTTestOptionKeys.keys)
            MSTPlayLoop.addData('MSTTestOptionKeys.corr', MSTTestOptionKeys.corr)
            if MSTTestOptionKeys.keys != None:  # we had a response
                MSTPlayLoop.addData('MSTTestOptionKeys.rt', MSTTestOptionKeys.rt)
            MSTPlayLoop.addData('MSTTestOptionKeys.started', MSTTestOptionKeys.tStartRefresh)
            MSTPlayLoop.addData('MSTTestOptionKeys.stopped', MSTTestOptionKeys.tStopRefresh)
            MSTPlayLoop.addData('MSTTestTrialNum.started', MSTTestTrialNum.tStartRefresh)
            MSTPlayLoop.addData('MSTTestTrialNum.stopped', MSTTestTrialNum.tStopRefresh)
            MSTPlayLoop.addData('MSTTestNote.started', MSTTestNote.tStartRefresh)
            MSTPlayLoop.addData('MSTTestNote.stopped', MSTTestNote.tStopRefresh)
            # the Routine "MSTplay" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'MSTPlayLoop'
        
        thisExp.nextEntry()
        
    # completed WordOrder repeats of 'MSTLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    SLLoop = data.TrialHandler(nReps=SLOrder, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='SLLoop')
    thisExp.addLoop(SLLoop)  # add the loop to the experiment
    thisSLLoop = SLLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSLLoop.rgb)
    if thisSLLoop != None:
        for paramName in thisSLLoop:
            exec('{} = thisSLLoop[paramName]'.format(paramName))
    
    for thisSLLoop in SLLoop:
        currentLoop = SLLoop
        # abbreviate parameter names if possible (e.g. rgb = thisSLLoop.rgb)
        if thisSLLoop != None:
            for paramName in thisSLLoop:
                exec('{} = thisSLLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "SLWelcome"-------
        continueRoutine = True
        # update component parameters for each repeat
        ContinueButton.keys = []
        ContinueButton.rt = []
        _ContinueButton_allKeys = []
        # keep track of which components have finished
        SLWelcomeComponents = [WelcomeMssg, ContinueButton, ContinueTxt]
        for thisComponent in SLWelcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SLWelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "SLWelcome"-------
        while continueRoutine:
            # get current time
            t = SLWelcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SLWelcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *WelcomeMssg* updates
            if WelcomeMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WelcomeMssg.frameNStart = frameN  # exact frame index
                WelcomeMssg.tStart = t  # local t and not account for scr refresh
                WelcomeMssg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WelcomeMssg, 'tStartRefresh')  # time at next scr refresh
                WelcomeMssg.setAutoDraw(True)
            
            # *ContinueButton* updates
            waitOnFlip = False
            if ContinueButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueButton.frameNStart = frameN  # exact frame index
                ContinueButton.tStart = t  # local t and not account for scr refresh
                ContinueButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueButton, 'tStartRefresh')  # time at next scr refresh
                ContinueButton.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ContinueButton.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ContinueButton.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ContinueButton.status == STARTED and not waitOnFlip:
                theseKeys = ContinueButton.getKeys(keyList=['space'], waitRelease=False)
                _ContinueButton_allKeys.extend(theseKeys)
                if len(_ContinueButton_allKeys):
                    ContinueButton.keys = _ContinueButton_allKeys[-1].name  # just the last key pressed
                    ContinueButton.rt = _ContinueButton_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *ContinueTxt* updates
            if ContinueTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueTxt.frameNStart = frameN  # exact frame index
                ContinueTxt.tStart = t  # local t and not account for scr refresh
                ContinueTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueTxt, 'tStartRefresh')  # time at next scr refresh
                ContinueTxt.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SLWelcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SLWelcome"-------
        for thisComponent in SLWelcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('WelcomeMssg.started', WelcomeMssg.tStartRefresh)
        SLLoop.addData('WelcomeMssg.stopped', WelcomeMssg.tStopRefresh)
        # check responses
        if ContinueButton.keys in ['', [], None]:  # No response was made
            ContinueButton.keys = None
        SLLoop.addData('ContinueButton.keys',ContinueButton.keys)
        if ContinueButton.keys != None:  # we had a response
            SLLoop.addData('ContinueButton.rt', ContinueButton.rt)
        SLLoop.addData('ContinueButton.started', ContinueButton.tStartRefresh)
        SLLoop.addData('ContinueButton.stopped', ContinueButton.tStopRefresh)
        SLLoop.addData('ContinueTxt.started', ContinueTxt.tStartRefresh)
        SLLoop.addData('ContinueTxt.stopped', ContinueTxt.tStopRefresh)
        # the Routine "SLWelcome" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ExposurePrep"-------
        continueRoutine = True
        # update component parameters for each repeat
        Randomization.addData('2', Condition)
        
        ExposureIntroKey.keys = []
        ExposureIntroKey.rt = []
        _ExposureIntroKey_allKeys = []
        # keep track of which components have finished
        ExposurePrepComponents = [ExposureIntro, ExposureIntroKey, ExposureIntroCont]
        for thisComponent in ExposurePrepComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ExposurePrepClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ExposurePrep"-------
        while continueRoutine:
            # get current time
            t = ExposurePrepClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ExposurePrepClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ExposureIntro* updates
            if ExposureIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ExposureIntro.frameNStart = frameN  # exact frame index
                ExposureIntro.tStart = t  # local t and not account for scr refresh
                ExposureIntro.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ExposureIntro, 'tStartRefresh')  # time at next scr refresh
                ExposureIntro.setAutoDraw(True)
            
            # *ExposureIntroKey* updates
            waitOnFlip = False
            if ExposureIntroKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ExposureIntroKey.frameNStart = frameN  # exact frame index
                ExposureIntroKey.tStart = t  # local t and not account for scr refresh
                ExposureIntroKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ExposureIntroKey, 'tStartRefresh')  # time at next scr refresh
                ExposureIntroKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ExposureIntroKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ExposureIntroKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ExposureIntroKey.status == STARTED and not waitOnFlip:
                theseKeys = ExposureIntroKey.getKeys(keyList=['space'], waitRelease=False)
                _ExposureIntroKey_allKeys.extend(theseKeys)
                if len(_ExposureIntroKey_allKeys):
                    ExposureIntroKey.keys = _ExposureIntroKey_allKeys[-1].name  # just the last key pressed
                    ExposureIntroKey.rt = _ExposureIntroKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *ExposureIntroCont* updates
            if ExposureIntroCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ExposureIntroCont.frameNStart = frameN  # exact frame index
                ExposureIntroCont.tStart = t  # local t and not account for scr refresh
                ExposureIntroCont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ExposureIntroCont, 'tStartRefresh')  # time at next scr refresh
                ExposureIntroCont.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ExposurePrepComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ExposurePrep"-------
        for thisComponent in ExposurePrepComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('ExposureIntro.started', ExposureIntro.tStartRefresh)
        SLLoop.addData('ExposureIntro.stopped', ExposureIntro.tStopRefresh)
        # check responses
        if ExposureIntroKey.keys in ['', [], None]:  # No response was made
            ExposureIntroKey.keys = None
        SLLoop.addData('ExposureIntroKey.keys',ExposureIntroKey.keys)
        if ExposureIntroKey.keys != None:  # we had a response
            SLLoop.addData('ExposureIntroKey.rt', ExposureIntroKey.rt)
        SLLoop.addData('ExposureIntroKey.started', ExposureIntroKey.tStartRefresh)
        SLLoop.addData('ExposureIntroKey.stopped', ExposureIntroKey.tStopRefresh)
        SLLoop.addData('ExposureIntroCont.started', ExposureIntroCont.tStartRefresh)
        SLLoop.addData('ExposureIntroCont.stopped', ExposureIntroCont.tStopRefresh)
        # the Routine "ExposurePrep" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        ExposureLoop = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(cond + "_new_list.xlsx", selection='0:1080'),
            seed=None, name='ExposureLoop')
        thisExp.addLoop(ExposureLoop)  # add the loop to the experiment
        thisExposureLoop = ExposureLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisExposureLoop.rgb)
        if thisExposureLoop != None:
            for paramName in thisExposureLoop:
                exec('{} = thisExposureLoop[paramName]'.format(paramName))
        
        for thisExposureLoop in ExposureLoop:
            currentLoop = ExposureLoop
            # abbreviate parameter names if possible (e.g. rgb = thisExposureLoop.rgb)
            if thisExposureLoop != None:
                for paramName in thisExposureLoop:
                    exec('{} = thisExposureLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Exposure"-------
            continueRoutine = True
            # update component parameters for each repeat
            scounter += 1
            
            if scounter == 57 or scounter == 123 or scounter == 147 or scounter == 177 or scounter == 267 or scounter == 300:
                pausecheck = 1
            else:
                pausecheck = 0
            
            if scounter == 360: #Restart counting every two minutes
                takebreak = 1
                scounter = 0
                volumecounter0 = 0
            else:
                takebreak = 0
            volumecounter0 += 1
            if volumecounter0 == 1 or volumecounter0 == 360:
                volume0 = 0.03
            elif volumecounter0 == 2 or volumecounter0 == 359:
                volume0 = 0.06
            elif volumecounter0 == 3 or volumecounter0 == 358:
                volume0 = 0.09
            elif volumecounter0 == 4 or volumecounter0 == 357:
                volume0 = 0.2
            elif volumecounter0 == 5 or volumecounter0 == 356:
                volume0 = 0.3
            elif volumecounter0 == 6 or volumecounter0 == 355:
                volume0 = 0.5
            else:
                volume0 = 1
            ExposurePlay.setSound(SyllableFile, hamming=True)
            ExposurePlay.setVolume(volume0, log=False)
            # keep track of which components have finished
            ExposureComponents = [ExposurePlay, ExposureCross, ExposureInstruction]
            for thisComponent in ExposureComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ExposureClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Exposure"-------
            while continueRoutine:
                # get current time
                t = ExposureClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ExposureClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop ExposurePlay
                if ExposurePlay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ExposurePlay.frameNStart = frameN  # exact frame index
                    ExposurePlay.tStart = t  # local t and not account for scr refresh
                    ExposurePlay.tStartRefresh = tThisFlipGlobal  # on global time
                    ExposurePlay.play(when=win)  # sync with win flip
                
                # *ExposureCross* updates
                if ExposureCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ExposureCross.frameNStart = frameN  # exact frame index
                    ExposureCross.tStart = t  # local t and not account for scr refresh
                    ExposureCross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ExposureCross, 'tStartRefresh')  # time at next scr refresh
                    ExposureCross.setAutoDraw(True)
                if ExposureCross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ExposureCross.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        ExposureCross.tStop = t  # not accounting for scr refresh
                        ExposureCross.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ExposureCross, 'tStopRefresh')  # time at next scr refresh
                        ExposureCross.setAutoDraw(False)
                
                # *ExposureInstruction* updates
                if ExposureInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ExposureInstruction.frameNStart = frameN  # exact frame index
                    ExposureInstruction.tStart = t  # local t and not account for scr refresh
                    ExposureInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ExposureInstruction, 'tStartRefresh')  # time at next scr refresh
                    ExposureInstruction.setAutoDraw(True)
                if ExposureInstruction.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ExposureInstruction.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        ExposureInstruction.tStop = t  # not accounting for scr refresh
                        ExposureInstruction.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(ExposureInstruction, 'tStopRefresh')  # time at next scr refresh
                        ExposureInstruction.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ExposureComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Exposure"-------
            for thisComponent in ExposureComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            ExposurePlay.stop()  # ensure sound has stopped at end of routine
            ExposureLoop.addData('ExposurePlay.started', ExposurePlay.tStartRefresh)
            ExposureLoop.addData('ExposurePlay.stopped', ExposurePlay.tStopRefresh)
            ExposureLoop.addData('ExposureCross.started', ExposureCross.tStartRefresh)
            ExposureLoop.addData('ExposureCross.stopped', ExposureCross.tStopRefresh)
            ExposureLoop.addData('ExposureInstruction.started', ExposureInstruction.tStartRefresh)
            ExposureLoop.addData('ExposureInstruction.stopped', ExposureInstruction.tStopRefresh)
            # the Routine "Exposure" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            PauseOnOff = data.TrialHandler(nReps=pausecheck, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='PauseOnOff')
            thisExp.addLoop(PauseOnOff)  # add the loop to the experiment
            thisPauseOnOff = PauseOnOff.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisPauseOnOff.rgb)
            if thisPauseOnOff != None:
                for paramName in thisPauseOnOff:
                    exec('{} = thisPauseOnOff[paramName]'.format(paramName))
            
            for thisPauseOnOff in PauseOnOff:
                currentLoop = PauseOnOff
                # abbreviate parameter names if possible (e.g. rgb = thisPauseOnOff.rgb)
                if thisPauseOnOff != None:
                    for paramName in thisPauseOnOff:
                        exec('{} = thisPauseOnOff[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "Pause"-------
                continueRoutine = True
                routineTimer.add(15.000000)
                # update component parameters for each repeat
                PauseCheckKey.keys = []
                PauseCheckKey.rt = []
                _PauseCheckKey_allKeys = []
                # keep track of which components have finished
                PauseComponents = [PauseCheckKey, PauseCross, PauseInstruction]
                for thisComponent in PauseComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                PauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Pause"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = PauseClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=PauseClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *PauseCheckKey* updates
                    waitOnFlip = False
                    if PauseCheckKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PauseCheckKey.frameNStart = frameN  # exact frame index
                        PauseCheckKey.tStart = t  # local t and not account for scr refresh
                        PauseCheckKey.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PauseCheckKey, 'tStartRefresh')  # time at next scr refresh
                        PauseCheckKey.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(PauseCheckKey.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(PauseCheckKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if PauseCheckKey.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > PauseCheckKey.tStartRefresh + 15-frameTolerance:
                            # keep track of stop time/frame for later
                            PauseCheckKey.tStop = t  # not accounting for scr refresh
                            PauseCheckKey.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(PauseCheckKey, 'tStopRefresh')  # time at next scr refresh
                            PauseCheckKey.status = FINISHED
                    if PauseCheckKey.status == STARTED and not waitOnFlip:
                        theseKeys = PauseCheckKey.getKeys(keyList=['space'], waitRelease=False)
                        _PauseCheckKey_allKeys.extend(theseKeys)
                        if len(_PauseCheckKey_allKeys):
                            PauseCheckKey.keys = _PauseCheckKey_allKeys[-1].name  # just the last key pressed
                            PauseCheckKey.rt = _PauseCheckKey_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *PauseCross* updates
                    if PauseCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PauseCross.frameNStart = frameN  # exact frame index
                        PauseCross.tStart = t  # local t and not account for scr refresh
                        PauseCross.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PauseCross, 'tStartRefresh')  # time at next scr refresh
                        PauseCross.setAutoDraw(True)
                    if PauseCross.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > PauseCross.tStartRefresh + 15-frameTolerance:
                            # keep track of stop time/frame for later
                            PauseCross.tStop = t  # not accounting for scr refresh
                            PauseCross.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(PauseCross, 'tStopRefresh')  # time at next scr refresh
                            PauseCross.setAutoDraw(False)
                    
                    # *PauseInstruction* updates
                    if PauseInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PauseInstruction.frameNStart = frameN  # exact frame index
                        PauseInstruction.tStart = t  # local t and not account for scr refresh
                        PauseInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PauseInstruction, 'tStartRefresh')  # time at next scr refresh
                        PauseInstruction.setAutoDraw(True)
                    if PauseInstruction.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > PauseInstruction.tStartRefresh + 15-frameTolerance:
                            # keep track of stop time/frame for later
                            PauseInstruction.tStop = t  # not accounting for scr refresh
                            PauseInstruction.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(PauseInstruction, 'tStopRefresh')  # time at next scr refresh
                            PauseInstruction.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in PauseComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Pause"-------
                for thisComponent in PauseComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if PauseCheckKey.keys in ['', [], None]:  # No response was made
                    PauseCheckKey.keys = None
                PauseOnOff.addData('PauseCheckKey.keys',PauseCheckKey.keys)
                if PauseCheckKey.keys != None:  # we had a response
                    PauseOnOff.addData('PauseCheckKey.rt', PauseCheckKey.rt)
                PauseOnOff.addData('PauseCheckKey.started', PauseCheckKey.tStartRefresh)
                PauseOnOff.addData('PauseCheckKey.stopped', PauseCheckKey.tStopRefresh)
                PauseOnOff.addData('PauseCross.started', PauseCross.tStartRefresh)
                PauseOnOff.addData('PauseCross.stopped', PauseCross.tStopRefresh)
                PauseOnOff.addData('PauseInstruction.started', PauseInstruction.tStartRefresh)
                PauseOnOff.addData('PauseInstruction.stopped', PauseInstruction.tStopRefresh)
                thisExp.nextEntry()
                
            # completed pausecheck repeats of 'PauseOnOff'
            
            
            # set up handler to look after randomisation of conditions etc
            BreakOnOff = data.TrialHandler(nReps=takebreak, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='BreakOnOff')
            thisExp.addLoop(BreakOnOff)  # add the loop to the experiment
            thisBreakOnOff = BreakOnOff.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisBreakOnOff.rgb)
            if thisBreakOnOff != None:
                for paramName in thisBreakOnOff:
                    exec('{} = thisBreakOnOff[paramName]'.format(paramName))
            
            for thisBreakOnOff in BreakOnOff:
                currentLoop = BreakOnOff
                # abbreviate parameter names if possible (e.g. rgb = thisBreakOnOff.rgb)
                if thisBreakOnOff != None:
                    for paramName in thisBreakOnOff:
                        exec('{} = thisBreakOnOff[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "TakeABreak"-------
                continueRoutine = True
                # update component parameters for each repeat
                BreakRespSubmit.keys = []
                BreakRespSubmit.rt = []
                _BreakRespSubmit_allKeys = []
                BreakResponse.setText(' \n')
                # keep track of which components have finished
                TakeABreakComponents = [BreakRespSubmit, BreakTxt, BreakResponse]
                for thisComponent in TakeABreakComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                TakeABreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "TakeABreak"-------
                while continueRoutine:
                    # get current time
                    t = TakeABreakClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=TakeABreakClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *BreakRespSubmit* updates
                    waitOnFlip = False
                    if BreakRespSubmit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        BreakRespSubmit.frameNStart = frameN  # exact frame index
                        BreakRespSubmit.tStart = t  # local t and not account for scr refresh
                        BreakRespSubmit.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(BreakRespSubmit, 'tStartRefresh')  # time at next scr refresh
                        BreakRespSubmit.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(BreakRespSubmit.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(BreakRespSubmit.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if BreakRespSubmit.status == STARTED and not waitOnFlip:
                        theseKeys = BreakRespSubmit.getKeys(keyList=['return'], waitRelease=False)
                        _BreakRespSubmit_allKeys.extend(theseKeys)
                        if len(_BreakRespSubmit_allKeys):
                            BreakRespSubmit.keys = _BreakRespSubmit_allKeys[-1].name  # just the last key pressed
                            BreakRespSubmit.rt = _BreakRespSubmit_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *BreakTxt* updates
                    if BreakTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        BreakTxt.frameNStart = frameN  # exact frame index
                        BreakTxt.tStart = t  # local t and not account for scr refresh
                        BreakTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(BreakTxt, 'tStartRefresh')  # time at next scr refresh
                        BreakTxt.setAutoDraw(True)
                    
                    # *BreakResponse* updates
                    if BreakResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        BreakResponse.frameNStart = frameN  # exact frame index
                        BreakResponse.tStart = t  # local t and not account for scr refresh
                        BreakResponse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(BreakResponse, 'tStartRefresh')  # time at next scr refresh
                        BreakResponse.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in TakeABreakComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "TakeABreak"-------
                for thisComponent in TakeABreakComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # check responses
                if BreakRespSubmit.keys in ['', [], None]:  # No response was made
                    BreakRespSubmit.keys = None
                BreakOnOff.addData('BreakRespSubmit.keys',BreakRespSubmit.keys)
                if BreakRespSubmit.keys != None:  # we had a response
                    BreakOnOff.addData('BreakRespSubmit.rt', BreakRespSubmit.rt)
                BreakOnOff.addData('BreakRespSubmit.started', BreakRespSubmit.tStartRefresh)
                BreakOnOff.addData('BreakRespSubmit.stopped', BreakRespSubmit.tStopRefresh)
                BreakOnOff.addData('BreakTxt.started', BreakTxt.tStartRefresh)
                BreakOnOff.addData('BreakTxt.stopped', BreakTxt.tStopRefresh)
                BreakOnOff.addData('BreakResponse.text',BreakResponse.text)
                BreakResponse.reset()
                BreakOnOff.addData('BreakResponse.started', BreakResponse.tStartRefresh)
                BreakOnOff.addData('BreakResponse.stopped', BreakResponse.tStopRefresh)
                # the Routine "TakeABreak" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "BreakOver"-------
                continueRoutine = True
                routineTimer.add(30.000000)
                # update component parameters for each repeat
                EndBreakKey.keys = []
                EndBreakKey.rt = []
                _EndBreakKey_allKeys = []
                # keep track of which components have finished
                BreakOverComponents = [EndBreakInstruction, EndBreakKey]
                for thisComponent in BreakOverComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                BreakOverClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "BreakOver"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = BreakOverClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=BreakOverClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *EndBreakInstruction* updates
                    if EndBreakInstruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        EndBreakInstruction.frameNStart = frameN  # exact frame index
                        EndBreakInstruction.tStart = t  # local t and not account for scr refresh
                        EndBreakInstruction.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(EndBreakInstruction, 'tStartRefresh')  # time at next scr refresh
                        EndBreakInstruction.setAutoDraw(True)
                    if EndBreakInstruction.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > EndBreakInstruction.tStartRefresh + 30-frameTolerance:
                            # keep track of stop time/frame for later
                            EndBreakInstruction.tStop = t  # not accounting for scr refresh
                            EndBreakInstruction.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(EndBreakInstruction, 'tStopRefresh')  # time at next scr refresh
                            EndBreakInstruction.setAutoDraw(False)
                    
                    # *EndBreakKey* updates
                    waitOnFlip = False
                    if EndBreakKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        EndBreakKey.frameNStart = frameN  # exact frame index
                        EndBreakKey.tStart = t  # local t and not account for scr refresh
                        EndBreakKey.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(EndBreakKey, 'tStartRefresh')  # time at next scr refresh
                        EndBreakKey.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(EndBreakKey.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(EndBreakKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if EndBreakKey.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > EndBreakKey.tStartRefresh + 30-frameTolerance:
                            # keep track of stop time/frame for later
                            EndBreakKey.tStop = t  # not accounting for scr refresh
                            EndBreakKey.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(EndBreakKey, 'tStopRefresh')  # time at next scr refresh
                            EndBreakKey.status = FINISHED
                    if EndBreakKey.status == STARTED and not waitOnFlip:
                        theseKeys = EndBreakKey.getKeys(keyList=['space'], waitRelease=False)
                        _EndBreakKey_allKeys.extend(theseKeys)
                        if len(_EndBreakKey_allKeys):
                            EndBreakKey.keys = _EndBreakKey_allKeys[-1].name  # just the last key pressed
                            EndBreakKey.rt = _EndBreakKey_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in BreakOverComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "BreakOver"-------
                for thisComponent in BreakOverComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                BreakOnOff.addData('EndBreakInstruction.started', EndBreakInstruction.tStartRefresh)
                BreakOnOff.addData('EndBreakInstruction.stopped', EndBreakInstruction.tStopRefresh)
                # check responses
                if EndBreakKey.keys in ['', [], None]:  # No response was made
                    EndBreakKey.keys = None
                BreakOnOff.addData('EndBreakKey.keys',EndBreakKey.keys)
                if EndBreakKey.keys != None:  # we had a response
                    BreakOnOff.addData('EndBreakKey.rt', EndBreakKey.rt)
                BreakOnOff.addData('EndBreakKey.started', EndBreakKey.tStartRefresh)
                BreakOnOff.addData('EndBreakKey.stopped', EndBreakKey.tStopRefresh)
                thisExp.nextEntry()
                
            # completed takebreak repeats of 'BreakOnOff'
            
            thisExp.nextEntry()
            
        # completed 1 repeats of 'ExposureLoop'
        
        
        # ------Prepare to start Routine "Part1Intro"-------
        continueRoutine = True
        # update component parameters for each repeat
        ContinueKey3.keys = []
        ContinueKey3.rt = []
        _ContinueKey3_allKeys = []
        # keep track of which components have finished
        Part1IntroComponents = [WelcomeTxt2, BeginTxt, ContinueKey3]
        for thisComponent in Part1IntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Part1IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Part1Intro"-------
        while continueRoutine:
            # get current time
            t = Part1IntroClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Part1IntroClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *WelcomeTxt2* updates
            if WelcomeTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WelcomeTxt2.frameNStart = frameN  # exact frame index
                WelcomeTxt2.tStart = t  # local t and not account for scr refresh
                WelcomeTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WelcomeTxt2, 'tStartRefresh')  # time at next scr refresh
                WelcomeTxt2.setAutoDraw(True)
            
            # *BeginTxt* updates
            if BeginTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BeginTxt.frameNStart = frameN  # exact frame index
                BeginTxt.tStart = t  # local t and not account for scr refresh
                BeginTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BeginTxt, 'tStartRefresh')  # time at next scr refresh
                BeginTxt.setAutoDraw(True)
            
            # *ContinueKey3* updates
            waitOnFlip = False
            if ContinueKey3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey3.frameNStart = frameN  # exact frame index
                ContinueKey3.tStart = t  # local t and not account for scr refresh
                ContinueKey3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey3, 'tStartRefresh')  # time at next scr refresh
                ContinueKey3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ContinueKey3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ContinueKey3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ContinueKey3.status == STARTED and not waitOnFlip:
                theseKeys = ContinueKey3.getKeys(keyList=['space'], waitRelease=False)
                _ContinueKey3_allKeys.extend(theseKeys)
                if len(_ContinueKey3_allKeys):
                    ContinueKey3.keys = _ContinueKey3_allKeys[-1].name  # just the last key pressed
                    ContinueKey3.rt = _ContinueKey3_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Part1IntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Part1Intro"-------
        for thisComponent in Part1IntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('WelcomeTxt2.started', WelcomeTxt2.tStartRefresh)
        SLLoop.addData('WelcomeTxt2.stopped', WelcomeTxt2.tStopRefresh)
        SLLoop.addData('BeginTxt.started', BeginTxt.tStartRefresh)
        SLLoop.addData('BeginTxt.stopped', BeginTxt.tStopRefresh)
        # check responses
        if ContinueKey3.keys in ['', [], None]:  # No response was made
            ContinueKey3.keys = None
        SLLoop.addData('ContinueKey3.keys',ContinueKey3.keys)
        if ContinueKey3.keys != None:  # we had a response
            SLLoop.addData('ContinueKey3.rt', ContinueKey3.rt)
        SLLoop.addData('ContinueKey3.started', ContinueKey3.tStartRefresh)
        SLLoop.addData('ContinueKey3.stopped', ContinueKey3.tStopRefresh)
        # the Routine "Part1Intro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "TDTrainingIntro"-------
        continueRoutine = True
        # update component parameters for each repeat
        TrainingContinueKey.keys = []
        TrainingContinueKey.rt = []
        _TrainingContinueKey_allKeys = []
        # keep track of which components have finished
        TDTrainingIntroComponents = [TrainingBeginTxt, TrainingContinueKey]
        for thisComponent in TDTrainingIntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TDTrainingIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TDTrainingIntro"-------
        while continueRoutine:
            # get current time
            t = TDTrainingIntroClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TDTrainingIntroClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrainingBeginTxt* updates
            if TrainingBeginTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrainingBeginTxt.frameNStart = frameN  # exact frame index
                TrainingBeginTxt.tStart = t  # local t and not account for scr refresh
                TrainingBeginTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrainingBeginTxt, 'tStartRefresh')  # time at next scr refresh
                TrainingBeginTxt.setAutoDraw(True)
            
            # *TrainingContinueKey* updates
            waitOnFlip = False
            if TrainingContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrainingContinueKey.frameNStart = frameN  # exact frame index
                TrainingContinueKey.tStart = t  # local t and not account for scr refresh
                TrainingContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrainingContinueKey, 'tStartRefresh')  # time at next scr refresh
                TrainingContinueKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TrainingContinueKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TrainingContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TrainingContinueKey.status == STARTED and not waitOnFlip:
                theseKeys = TrainingContinueKey.getKeys(keyList=['space'], waitRelease=False)
                _TrainingContinueKey_allKeys.extend(theseKeys)
                if len(_TrainingContinueKey_allKeys):
                    TrainingContinueKey.keys = _TrainingContinueKey_allKeys[-1].name  # just the last key pressed
                    TrainingContinueKey.rt = _TrainingContinueKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TDTrainingIntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TDTrainingIntro"-------
        for thisComponent in TDTrainingIntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('TrainingBeginTxt.started', TrainingBeginTxt.tStartRefresh)
        SLLoop.addData('TrainingBeginTxt.stopped', TrainingBeginTxt.tStopRefresh)
        # check responses
        if TrainingContinueKey.keys in ['', [], None]:  # No response was made
            TrainingContinueKey.keys = None
        SLLoop.addData('TrainingContinueKey.keys',TrainingContinueKey.keys)
        if TrainingContinueKey.keys != None:  # we had a response
            SLLoop.addData('TrainingContinueKey.rt', TrainingContinueKey.rt)
        SLLoop.addData('TrainingContinueKey.started', TrainingContinueKey.tStartRefresh)
        SLLoop.addData('TrainingContinueKey.stopped', TrainingContinueKey.tStopRefresh)
        # the Routine "TDTrainingIntro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        TrainTDLoop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('TargetSyllables.xlsx', selection='216:218'),
            seed=None, name='TrainTDLoop')
        thisExp.addLoop(TrainTDLoop)  # add the loop to the experiment
        thisTrainTDLoop = TrainTDLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrainTDLoop.rgb)
        if thisTrainTDLoop != None:
            for paramName in thisTrainTDLoop:
                exec('{} = thisTrainTDLoop[paramName]'.format(paramName))
        
        for thisTrainTDLoop in TrainTDLoop:
            currentLoop = TrainTDLoop
            # abbreviate parameter names if possible (e.g. rgb = thisTrainTDLoop.rgb)
            if thisTrainTDLoop != None:
                for paramName in thisTrainTDLoop:
                    exec('{} = thisTrainTDLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "TrainingSample"-------
            continueRoutine = True
            # update component parameters for each repeat
            TrainigTarget.setText(Target)
            trainingcount += 1
            
            TrainingNumber.setText('Training ' + str(trainingcount) )
            TSContinueKey.keys = []
            TSContinueKey.rt = []
            _TSContinueKey_allKeys = []
            # keep track of which components have finished
            TrainingSampleComponents = [SampleMssg2, TrainigTarget, TrainingNumber, TrainingSampleContinue, TSContinueKey]
            for thisComponent in TrainingSampleComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TrainingSampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TrainingSample"-------
            while continueRoutine:
                # get current time
                t = TrainingSampleClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TrainingSampleClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *SampleMssg2* updates
                if SampleMssg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SampleMssg2.frameNStart = frameN  # exact frame index
                    SampleMssg2.tStart = t  # local t and not account for scr refresh
                    SampleMssg2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SampleMssg2, 'tStartRefresh')  # time at next scr refresh
                    SampleMssg2.setAutoDraw(True)
                
                # *TrainigTarget* updates
                if TrainigTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainigTarget.frameNStart = frameN  # exact frame index
                    TrainigTarget.tStart = t  # local t and not account for scr refresh
                    TrainigTarget.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainigTarget, 'tStartRefresh')  # time at next scr refresh
                    TrainigTarget.setAutoDraw(True)
                
                # *TrainingNumber* updates
                if TrainingNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainingNumber.frameNStart = frameN  # exact frame index
                    TrainingNumber.tStart = t  # local t and not account for scr refresh
                    TrainingNumber.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainingNumber, 'tStartRefresh')  # time at next scr refresh
                    TrainingNumber.setAutoDraw(True)
                
                # *TrainingSampleContinue* updates
                if TrainingSampleContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainingSampleContinue.frameNStart = frameN  # exact frame index
                    TrainingSampleContinue.tStart = t  # local t and not account for scr refresh
                    TrainingSampleContinue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainingSampleContinue, 'tStartRefresh')  # time at next scr refresh
                    TrainingSampleContinue.setAutoDraw(True)
                
                # *TSContinueKey* updates
                waitOnFlip = False
                if TSContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TSContinueKey.frameNStart = frameN  # exact frame index
                    TSContinueKey.tStart = t  # local t and not account for scr refresh
                    TSContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TSContinueKey, 'tStartRefresh')  # time at next scr refresh
                    TSContinueKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(TSContinueKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(TSContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if TSContinueKey.status == STARTED and not waitOnFlip:
                    theseKeys = TSContinueKey.getKeys(keyList=['space'], waitRelease=False)
                    _TSContinueKey_allKeys.extend(theseKeys)
                    if len(_TSContinueKey_allKeys):
                        TSContinueKey.keys = _TSContinueKey_allKeys[-1].name  # just the last key pressed
                        TSContinueKey.rt = _TSContinueKey_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TrainingSampleComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TrainingSample"-------
            for thisComponent in TrainingSampleComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrainTDLoop.addData('SampleMssg2.started', SampleMssg2.tStartRefresh)
            TrainTDLoop.addData('SampleMssg2.stopped', SampleMssg2.tStopRefresh)
            TrainTDLoop.addData('TrainigTarget.started', TrainigTarget.tStartRefresh)
            TrainTDLoop.addData('TrainigTarget.stopped', TrainigTarget.tStopRefresh)
            TrainTDLoop.addData('TrainingNumber.started', TrainingNumber.tStartRefresh)
            TrainTDLoop.addData('TrainingNumber.stopped', TrainingNumber.tStopRefresh)
            TrainTDLoop.addData('TrainingSampleContinue.started', TrainingSampleContinue.tStartRefresh)
            TrainTDLoop.addData('TrainingSampleContinue.stopped', TrainingSampleContinue.tStopRefresh)
            # check responses
            if TSContinueKey.keys in ['', [], None]:  # No response was made
                TSContinueKey.keys = None
            TrainTDLoop.addData('TSContinueKey.keys',TSContinueKey.keys)
            if TSContinueKey.keys != None:  # we had a response
                TrainTDLoop.addData('TSContinueKey.rt', TSContinueKey.rt)
            TrainTDLoop.addData('TSContinueKey.started', TSContinueKey.tStartRefresh)
            TrainTDLoop.addData('TSContinueKey.stopped', TSContinueKey.tStopRefresh)
            # the Routine "TrainingSample" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "TrainingPlaySample"-------
            continueRoutine = True
            # update component parameters for each repeat
            TrainingSampleSound.setSound(TargetFile, hamming=True)
            TrainingSampleSound.setVolume(0.3, log=False)
            TraingRepeatSound.setSound(TargetFile, hamming=True)
            TraingRepeatSound.setVolume(0.3, log=False)
            TrainTargetTxt.setText(Target)
            TrainingNumber2.setText('Training ' + str(trainingcount) )
            TrainEndSample.keys = []
            TrainEndSample.rt = []
            _TrainEndSample_allKeys = []
            # keep track of which components have finished
            TrainingPlaySampleComponents = [TrainingSampleSound, TraingRepeatSound, TrainTargetTxt, text_5, TrainingBeginSample, TrainingNumber2, TrainEndSample]
            for thisComponent in TrainingPlaySampleComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TrainingPlaySampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TrainingPlaySample"-------
            while continueRoutine:
                # get current time
                t = TrainingPlaySampleClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TrainingPlaySampleClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop TrainingSampleSound
                if TrainingSampleSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainingSampleSound.frameNStart = frameN  # exact frame index
                    TrainingSampleSound.tStart = t  # local t and not account for scr refresh
                    TrainingSampleSound.tStartRefresh = tThisFlipGlobal  # on global time
                    TrainingSampleSound.play(when=win)  # sync with win flip
                # start/stop TraingRepeatSound
                if TraingRepeatSound.status == NOT_STARTED and tThisFlip >= TrainingSampleSound.getDuration() + 1-frameTolerance:
                    # keep track of start time/frame for later
                    TraingRepeatSound.frameNStart = frameN  # exact frame index
                    TraingRepeatSound.tStart = t  # local t and not account for scr refresh
                    TraingRepeatSound.tStartRefresh = tThisFlipGlobal  # on global time
                    TraingRepeatSound.play(when=win)  # sync with win flip
                
                # *TrainTargetTxt* updates
                if TrainTargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainTargetTxt.frameNStart = frameN  # exact frame index
                    TrainTargetTxt.tStart = t  # local t and not account for scr refresh
                    TrainTargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainTargetTxt, 'tStartRefresh')  # time at next scr refresh
                    TrainTargetTxt.setAutoDraw(True)
                
                # *text_5* updates
                if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(True)
                
                # *TrainingBeginSample* updates
                if TrainingBeginSample.status == NOT_STARTED and tThisFlip >= TrainingSampleSound.getDuration() +1-frameTolerance:
                    # keep track of start time/frame for later
                    TrainingBeginSample.frameNStart = frameN  # exact frame index
                    TrainingBeginSample.tStart = t  # local t and not account for scr refresh
                    TrainingBeginSample.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainingBeginSample, 'tStartRefresh')  # time at next scr refresh
                    TrainingBeginSample.setAutoDraw(True)
                
                # *TrainingNumber2* updates
                if TrainingNumber2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainingNumber2.frameNStart = frameN  # exact frame index
                    TrainingNumber2.tStart = t  # local t and not account for scr refresh
                    TrainingNumber2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainingNumber2, 'tStartRefresh')  # time at next scr refresh
                    TrainingNumber2.setAutoDraw(True)
                
                # *TrainEndSample* updates
                waitOnFlip = False
                if TrainEndSample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainEndSample.frameNStart = frameN  # exact frame index
                    TrainEndSample.tStart = t  # local t and not account for scr refresh
                    TrainEndSample.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainEndSample, 'tStartRefresh')  # time at next scr refresh
                    TrainEndSample.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(TrainEndSample.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(TrainEndSample.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if TrainEndSample.status == STARTED and not waitOnFlip:
                    theseKeys = TrainEndSample.getKeys(keyList=['space'], waitRelease=False)
                    _TrainEndSample_allKeys.extend(theseKeys)
                    if len(_TrainEndSample_allKeys):
                        TrainEndSample.keys = _TrainEndSample_allKeys[-1].name  # just the last key pressed
                        TrainEndSample.rt = _TrainEndSample_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TrainingPlaySampleComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TrainingPlaySample"-------
            for thisComponent in TrainingPlaySampleComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrainingSampleSound.stop()  # ensure sound has stopped at end of routine
            TrainTDLoop.addData('TrainingSampleSound.started', TrainingSampleSound.tStartRefresh)
            TrainTDLoop.addData('TrainingSampleSound.stopped', TrainingSampleSound.tStopRefresh)
            TraingRepeatSound.stop()  # ensure sound has stopped at end of routine
            TrainTDLoop.addData('TraingRepeatSound.started', TraingRepeatSound.tStartRefresh)
            TrainTDLoop.addData('TraingRepeatSound.stopped', TraingRepeatSound.tStopRefresh)
            TrainTDLoop.addData('TrainTargetTxt.started', TrainTargetTxt.tStartRefresh)
            TrainTDLoop.addData('TrainTargetTxt.stopped', TrainTargetTxt.tStopRefresh)
            TrainTDLoop.addData('text_5.started', text_5.tStartRefresh)
            TrainTDLoop.addData('text_5.stopped', text_5.tStopRefresh)
            TrainTDLoop.addData('TrainingBeginSample.started', TrainingBeginSample.tStartRefresh)
            TrainTDLoop.addData('TrainingBeginSample.stopped', TrainingBeginSample.tStopRefresh)
            TrainTDLoop.addData('TrainingNumber2.started', TrainingNumber2.tStartRefresh)
            TrainTDLoop.addData('TrainingNumber2.stopped', TrainingNumber2.tStopRefresh)
            # check responses
            if TrainEndSample.keys in ['', [], None]:  # No response was made
                TrainEndSample.keys = None
            TrainTDLoop.addData('TrainEndSample.keys',TrainEndSample.keys)
            if TrainEndSample.keys != None:  # we had a response
                TrainTDLoop.addData('TrainEndSample.rt', TrainEndSample.rt)
            TrainTDLoop.addData('TrainEndSample.started', TrainEndSample.tStartRefresh)
            TrainTDLoop.addData('TrainEndSample.stopped', TrainEndSample.tStopRefresh)
            # the Routine "TrainingPlaySample" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "TrainStart"-------
            continueRoutine = True
            routineTimer.add(3.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            TrainStartComponents = [Three, Two, text]
            for thisComponent in TrainStartComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TrainStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TrainStart"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = TrainStartClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TrainStartClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Three* updates
                if Three.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Three.frameNStart = frameN  # exact frame index
                    Three.tStart = t  # local t and not account for scr refresh
                    Three.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Three, 'tStartRefresh')  # time at next scr refresh
                    Three.setAutoDraw(True)
                if Three.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Three.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Three.tStop = t  # not accounting for scr refresh
                        Three.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Three, 'tStopRefresh')  # time at next scr refresh
                        Three.setAutoDraw(False)
                
                # *Two* updates
                if Two.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    Two.frameNStart = frameN  # exact frame index
                    Two.tStart = t  # local t and not account for scr refresh
                    Two.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Two, 'tStartRefresh')  # time at next scr refresh
                    Two.setAutoDraw(True)
                if Two.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Two.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Two.tStop = t  # not accounting for scr refresh
                        Two.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Two, 'tStopRefresh')  # time at next scr refresh
                        Two.setAutoDraw(False)
                
                # *text* updates
                if text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    text.setAutoDraw(True)
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                        text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TrainStartComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TrainStart"-------
            for thisComponent in TrainStartComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrainTDLoop.addData('Three.started', Three.tStartRefresh)
            TrainTDLoop.addData('Three.stopped', Three.tStopRefresh)
            TrainTDLoop.addData('Two.started', Two.tStartRefresh)
            TrainTDLoop.addData('Two.stopped', Two.tStopRefresh)
            TrainTDLoop.addData('text.started', text.tStartRefresh)
            TrainTDLoop.addData('text.stopped', text.tStopRefresh)
            
            # set up handler to look after randomisation of conditions etc
            TrainTD = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('TDTrainList.xlsx', selection='0:45'),
                seed=None, name='TrainTD')
            thisExp.addLoop(TrainTD)  # add the loop to the experiment
            thisTrainTD = TrainTD.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrainTD.rgb)
            if thisTrainTD != None:
                for paramName in thisTrainTD:
                    exec('{} = thisTrainTD[paramName]'.format(paramName))
            
            for thisTrainTD in TrainTD:
                currentLoop = TrainTD
                # abbreviate parameter names if possible (e.g. rgb = thisTrainTD.rgb)
                if thisTrainTD != None:
                    for paramName in thisTrainTD:
                        exec('{} = thisTrainTD[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "train"-------
                continueRoutine = True
                # update component parameters for each repeat
                if Sound == Target:
                    TargetOnset = mytimer.getTime()
                soundOnset = mytimer.getTime()
                
                TDTrainSound.setSound(File, hamming=True)
                TDTrainSound.setVolume(0.3, log=False)
                TrainResp.keys = []
                TrainResp.rt = []
                _TrainResp_allKeys = []
                Cross3.setText(Target)
                # keep track of which components have finished
                trainComponents = [TDTrainSound, TrainResp, TDTrainTxt, Cross3]
                for thisComponent in trainComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "train"-------
                while continueRoutine:
                    # get current time
                    t = trainClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=trainClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # start/stop TDTrainSound
                    if TDTrainSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TDTrainSound.frameNStart = frameN  # exact frame index
                        TDTrainSound.tStart = t  # local t and not account for scr refresh
                        TDTrainSound.tStartRefresh = tThisFlipGlobal  # on global time
                        TDTrainSound.play(when=win)  # sync with win flip
                    
                    # *TrainResp* updates
                    waitOnFlip = False
                    if TrainResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TrainResp.frameNStart = frameN  # exact frame index
                        TrainResp.tStart = t  # local t and not account for scr refresh
                        TrainResp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TrainResp, 'tStartRefresh')  # time at next scr refresh
                        TrainResp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(TrainResp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(TrainResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if TrainResp.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > TrainResp.tStartRefresh + TDTrainSound.getDuration()+0.03-frameTolerance:
                            # keep track of stop time/frame for later
                            TrainResp.tStop = t  # not accounting for scr refresh
                            TrainResp.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(TrainResp, 'tStopRefresh')  # time at next scr refresh
                            TrainResp.status = FINISHED
                    if TrainResp.status == STARTED and not waitOnFlip:
                        theseKeys = TrainResp.getKeys(keyList=['space'], waitRelease=False)
                        _TrainResp_allKeys.extend(theseKeys)
                        if len(_TrainResp_allKeys):
                            TrainResp.keys = [key.name for key in _TrainResp_allKeys]  # storing all keys
                            TrainResp.rt = [key.rt for key in _TrainResp_allKeys]
                    
                    # *TDTrainTxt* updates
                    if TDTrainTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TDTrainTxt.frameNStart = frameN  # exact frame index
                        TDTrainTxt.tStart = t  # local t and not account for scr refresh
                        TDTrainTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TDTrainTxt, 'tStartRefresh')  # time at next scr refresh
                        TDTrainTxt.setAutoDraw(True)
                    if TDTrainTxt.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > TDTrainTxt.tStartRefresh + TDTrainSound.getDuration()+0.05-frameTolerance:
                            # keep track of stop time/frame for later
                            TDTrainTxt.tStop = t  # not accounting for scr refresh
                            TDTrainTxt.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(TDTrainTxt, 'tStopRefresh')  # time at next scr refresh
                            TDTrainTxt.setAutoDraw(False)
                    
                    # *Cross3* updates
                    if Cross3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Cross3.frameNStart = frameN  # exact frame index
                        Cross3.tStart = t  # local t and not account for scr refresh
                        Cross3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Cross3, 'tStartRefresh')  # time at next scr refresh
                        Cross3.setAutoDraw(True)
                    if Cross3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Cross3.tStartRefresh + TDTrainSound.getDuration()+0.05-frameTolerance:
                            # keep track of stop time/frame for later
                            Cross3.tStop = t  # not accounting for scr refresh
                            Cross3.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(Cross3, 'tStopRefresh')  # time at next scr refresh
                            Cross3.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trainComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "train"-------
                for thisComponent in trainComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # Set Target Onset time
                #if Sound == Target:
                #    TargetOnset = TDTrainSound.tStartRefresh
                TrainTD.addData('TargetOnset', TargetOnset)
                # Check if keyboard has been pressed
                if TrainResp.keys in ['', [], None]:
                    TrainResp.keys = None
                if TrainResp.keys != None: # we had a response
                    #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
                    respOnset = TrainResp.rt[0] + soundOnset
                    TrainTD.addData('RespOnset', respOnset)
                    # Check if the response is too close to the previous valid response
                    if respOnset - previousOnset > 1.2:
                        # Calculate RT
                        reactiontime = respOnset - TargetOnset
                        TrainTD.addData('ReactionTime', reactiontime)
                        # Check if RT is below the cutoff
                        if reactiontime < 1.2:
                            # Count it as a valid "hit"
                            respcount += 1
                            # Count the RT toward total RTs
                            TrainRT += reactiontime
                            # Use this as the latest valid response
                            previousOnset = respOnset
                # Calculate the mean RT
                if respcount > 0:
                    meanRT = TrainRT/respcount
                    TrainTD.addData('mean.rt', meanRT)
                else: # If no response was made
                    meanRT = 0
                # If too many responses were made     
                if respcount > 5:
                    respcount = 5
                    
                TrainTD.addData('RespOnset', respOnset)
                TrainTD.addData('Respcount', respcount)
                
                TDTrainSound.stop()  # ensure sound has stopped at end of routine
                TrainTD.addData('TDTrainSound.started', TDTrainSound.tStartRefresh)
                TrainTD.addData('TDTrainSound.stopped', TDTrainSound.tStopRefresh)
                # check responses
                if TrainResp.keys in ['', [], None]:  # No response was made
                    TrainResp.keys = None
                TrainTD.addData('TrainResp.keys',TrainResp.keys)
                if TrainResp.keys != None:  # we had a response
                    TrainTD.addData('TrainResp.rt', TrainResp.rt)
                TrainTD.addData('TrainResp.started', TrainResp.tStartRefresh)
                TrainTD.addData('TrainResp.stopped', TrainResp.tStopRefresh)
                TrainTD.addData('TDTrainTxt.started', TDTrainTxt.tStartRefresh)
                TrainTD.addData('TDTrainTxt.stopped', TDTrainTxt.tStopRefresh)
                TrainTD.addData('Cross3.started', Cross3.tStartRefresh)
                TrainTD.addData('Cross3.stopped', Cross3.tStopRefresh)
                # the Routine "train" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'TrainTD'
            
            
            # ------Prepare to start Routine "Pause1sec"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Pause1secComponents = [PauseTxt2]
            for thisComponent in Pause1secComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Pause1secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Pause1sec"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Pause1secClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Pause1secClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PauseTxt2* updates
                if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PauseTxt2.frameNStart = frameN  # exact frame index
                    PauseTxt2.tStart = t  # local t and not account for scr refresh
                    PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                    PauseTxt2.setAutoDraw(True)
                if PauseTxt2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        PauseTxt2.tStop = t  # not accounting for scr refresh
                        PauseTxt2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(PauseTxt2, 'tStopRefresh')  # time at next scr refresh
                        PauseTxt2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Pause1secComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Pause1sec"-------
            for thisComponent in Pause1secComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrainTDLoop.addData('PauseTxt2.started', PauseTxt2.tStartRefresh)
            TrainTDLoop.addData('PauseTxt2.stopped', PauseTxt2.tStopRefresh)
            
            # ------Prepare to start Routine "TDTrainFeedback"-------
            continueRoutine = True
            # update component parameters for each repeat
            TDTrainFeedbackMssg.setText('You correctly responded to ' + str(respcount) + ' of the 5 target syllables. Your average response time was '+ str(round(meanRT, 2)) + 's.'  )
            EndFeedback.keys = []
            EndFeedback.rt = []
            _EndFeedback_allKeys = []
            # keep track of which components have finished
            TDTrainFeedbackComponents = [TDTrainFeedbackMssg, EndFeedback, TrainingContinue]
            for thisComponent in TDTrainFeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TDTrainFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "TDTrainFeedback"-------
            while continueRoutine:
                # get current time
                t = TDTrainFeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TDTrainFeedbackClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *TDTrainFeedbackMssg* updates
                if TDTrainFeedbackMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TDTrainFeedbackMssg.frameNStart = frameN  # exact frame index
                    TDTrainFeedbackMssg.tStart = t  # local t and not account for scr refresh
                    TDTrainFeedbackMssg.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TDTrainFeedbackMssg, 'tStartRefresh')  # time at next scr refresh
                    TDTrainFeedbackMssg.setAutoDraw(True)
                
                # *EndFeedback* updates
                waitOnFlip = False
                if EndFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    EndFeedback.frameNStart = frameN  # exact frame index
                    EndFeedback.tStart = t  # local t and not account for scr refresh
                    EndFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(EndFeedback, 'tStartRefresh')  # time at next scr refresh
                    EndFeedback.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(EndFeedback.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(EndFeedback.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if EndFeedback.status == STARTED and not waitOnFlip:
                    theseKeys = EndFeedback.getKeys(keyList=['space'], waitRelease=False)
                    _EndFeedback_allKeys.extend(theseKeys)
                    if len(_EndFeedback_allKeys):
                        EndFeedback.keys = _EndFeedback_allKeys[-1].name  # just the last key pressed
                        EndFeedback.rt = _EndFeedback_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *TrainingContinue* updates
                if TrainingContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TrainingContinue.frameNStart = frameN  # exact frame index
                    TrainingContinue.tStart = t  # local t and not account for scr refresh
                    TrainingContinue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TrainingContinue, 'tStartRefresh')  # time at next scr refresh
                    TrainingContinue.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TDTrainFeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "TDTrainFeedback"-------
            for thisComponent in TDTrainFeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            TrainTDLoop.addData('TDTrainFeedbackMssg.started', TDTrainFeedbackMssg.tStartRefresh)
            TrainTDLoop.addData('TDTrainFeedbackMssg.stopped', TDTrainFeedbackMssg.tStopRefresh)
            # check responses
            if EndFeedback.keys in ['', [], None]:  # No response was made
                EndFeedback.keys = None
            TrainTDLoop.addData('EndFeedback.keys',EndFeedback.keys)
            if EndFeedback.keys != None:  # we had a response
                TrainTDLoop.addData('EndFeedback.rt', EndFeedback.rt)
            TrainTDLoop.addData('EndFeedback.started', EndFeedback.tStartRefresh)
            TrainTDLoop.addData('EndFeedback.stopped', EndFeedback.tStopRefresh)
            respcount = 0
            reactiontime = 0
            TrainRT = 0
            TrainTDLoop.addData('TrainingContinue.started', TrainingContinue.tStartRefresh)
            TrainTDLoop.addData('TrainingContinue.stopped', TrainingContinue.tStopRefresh)
            # the Routine "TDTrainFeedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'TrainTDLoop'
        
        
        # ------Prepare to start Routine "P1IntroII"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        if cond == "1":
            partone = "0:12"
            parttwo = "12:24"
            partthree = "24:36"
        elif cond == "X":
            partone = "36:48"
            parttwo = "48:60"
            partthree = "60:72"
        elif cond == "2":
            partone = "72:84"
            parttwo = "84:96"
            partthree = "96:108"
        elif cond == "4":
            partone = "108:120"
            parttwo = "120:132"
            partthree = "132:144"
        elif cond == "3":
            partone = "144:156"
            parttwo = "156:168"
            partthree = "168:180"
        elif cond == "6":
            partone = "180:192"
            parttwo = "192:204"
            partthree = "204:216"
        
        import random
        partlist = [partone, parttwo, partthree]
        random.shuffle(partlist)
        first = partlist[0] 
        second = partlist[1]
        third = partlist[2]
            
        # keep track of which components have finished
        P1IntroIIComponents = [P1Intro2Txt, text_4, key_resp]
        for thisComponent in P1IntroIIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        P1IntroIIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "P1IntroII"-------
        while continueRoutine:
            # get current time
            t = P1IntroIIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=P1IntroIIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *P1Intro2Txt* updates
            if P1Intro2Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P1Intro2Txt.frameNStart = frameN  # exact frame index
                P1Intro2Txt.tStart = t  # local t and not account for scr refresh
                P1Intro2Txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P1Intro2Txt, 'tStartRefresh')  # time at next scr refresh
                P1Intro2Txt.setAutoDraw(True)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in P1IntroIIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "P1IntroII"-------
        for thisComponent in P1IntroIIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('P1Intro2Txt.started', P1Intro2Txt.tStartRefresh)
        SLLoop.addData('P1Intro2Txt.stopped', P1Intro2Txt.tStopRefresh)
        SLLoop.addData('text_4.started', text_4.tStartRefresh)
        SLLoop.addData('text_4.stopped', text_4.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        SLLoop.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            SLLoop.addData('key_resp.rt', key_resp.rt)
        SLLoop.addData('key_resp.started', key_resp.tStartRefresh)
        SLLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "P1IntroII" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        TD = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='TD')
        thisExp.addLoop(TD)  # add the loop to the experiment
        thisTD = TD.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTD.rgb)
        if thisTD != None:
            for paramName in thisTD:
                exec('{} = thisTD[paramName]'.format(paramName))
        
        for thisTD in TD:
            currentLoop = TD
            # abbreviate parameter names if possible (e.g. rgb = thisTD.rgb)
            if thisTD != None:
                for paramName in thisTD:
                    exec('{} = thisTD[paramName]'.format(paramName))
            
            # set up handler to look after randomisation of conditions etc
            FirstTDLoop = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('TargetSyllables.xlsx', selection=first),
                seed=None, name='FirstTDLoop')
            thisExp.addLoop(FirstTDLoop)  # add the loop to the experiment
            thisFirstTDLoop = FirstTDLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisFirstTDLoop.rgb)
            if thisFirstTDLoop != None:
                for paramName in thisFirstTDLoop:
                    exec('{} = thisFirstTDLoop[paramName]'.format(paramName))
            
            for thisFirstTDLoop in FirstTDLoop:
                currentLoop = FirstTDLoop
                # abbreviate parameter names if possible (e.g. rgb = thisFirstTDLoop.rgb)
                if thisFirstTDLoop != None:
                    for paramName in thisFirstTDLoop:
                        exec('{} = thisFirstTDLoop[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "SampleIntro"-------
                continueRoutine = True
                # update component parameters for each repeat
                PlayTargetKey.keys = []
                PlayTargetKey.rt = []
                _PlayTargetKey_allKeys = []
                TargetTxt.setText(Target)
                repeatCount += 1
                TrialNo = "Recording " + str(repeatCount) + " of 36"
                TrialNoTxt.setText(TrialNo)
                # keep track of which components have finished
                SampleIntroComponents = [TargetMssg, PlayTargetKey, TargetTxt, TrialNoTxt, ContinueTxt4]
                for thisComponent in SampleIntroComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                SampleIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "SampleIntro"-------
                while continueRoutine:
                    # get current time
                    t = SampleIntroClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=SampleIntroClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *TargetMssg* updates
                    if TargetMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TargetMssg.frameNStart = frameN  # exact frame index
                        TargetMssg.tStart = t  # local t and not account for scr refresh
                        TargetMssg.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TargetMssg, 'tStartRefresh')  # time at next scr refresh
                        TargetMssg.setAutoDraw(True)
                    
                    # *PlayTargetKey* updates
                    waitOnFlip = False
                    if PlayTargetKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PlayTargetKey.frameNStart = frameN  # exact frame index
                        PlayTargetKey.tStart = t  # local t and not account for scr refresh
                        PlayTargetKey.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PlayTargetKey, 'tStartRefresh')  # time at next scr refresh
                        PlayTargetKey.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(PlayTargetKey.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(PlayTargetKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if PlayTargetKey.status == STARTED and not waitOnFlip:
                        theseKeys = PlayTargetKey.getKeys(keyList=['space'], waitRelease=False)
                        _PlayTargetKey_allKeys.extend(theseKeys)
                        if len(_PlayTargetKey_allKeys):
                            PlayTargetKey.keys = _PlayTargetKey_allKeys[-1].name  # just the last key pressed
                            PlayTargetKey.rt = _PlayTargetKey_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *TargetTxt* updates
                    if TargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TargetTxt.frameNStart = frameN  # exact frame index
                        TargetTxt.tStart = t  # local t and not account for scr refresh
                        TargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TargetTxt, 'tStartRefresh')  # time at next scr refresh
                        TargetTxt.setAutoDraw(True)
                    
                    # *TrialNoTxt* updates
                    if TrialNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TrialNoTxt.frameNStart = frameN  # exact frame index
                        TrialNoTxt.tStart = t  # local t and not account for scr refresh
                        TrialNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TrialNoTxt, 'tStartRefresh')  # time at next scr refresh
                        TrialNoTxt.setAutoDraw(True)
                    
                    # *ContinueTxt4* updates
                    if ContinueTxt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        ContinueTxt4.frameNStart = frameN  # exact frame index
                        ContinueTxt4.tStart = t  # local t and not account for scr refresh
                        ContinueTxt4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(ContinueTxt4, 'tStartRefresh')  # time at next scr refresh
                        ContinueTxt4.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in SampleIntroComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "SampleIntro"-------
                for thisComponent in SampleIntroComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                FirstTDLoop.addData('TargetMssg.started', TargetMssg.tStartRefresh)
                FirstTDLoop.addData('TargetMssg.stopped', TargetMssg.tStopRefresh)
                # check responses
                if PlayTargetKey.keys in ['', [], None]:  # No response was made
                    PlayTargetKey.keys = None
                FirstTDLoop.addData('PlayTargetKey.keys',PlayTargetKey.keys)
                if PlayTargetKey.keys != None:  # we had a response
                    FirstTDLoop.addData('PlayTargetKey.rt', PlayTargetKey.rt)
                FirstTDLoop.addData('PlayTargetKey.started', PlayTargetKey.tStartRefresh)
                FirstTDLoop.addData('PlayTargetKey.stopped', PlayTargetKey.tStopRefresh)
                FirstTDLoop.addData('TargetTxt.started', TargetTxt.tStartRefresh)
                FirstTDLoop.addData('TargetTxt.stopped', TargetTxt.tStopRefresh)
                FirstTDLoop.addData('TrialNoTxt.started', TrialNoTxt.tStartRefresh)
                FirstTDLoop.addData('TrialNoTxt.stopped', TrialNoTxt.tStopRefresh)
                FirstTDLoop.addData('ContinueTxt4.started', ContinueTxt4.tStartRefresh)
                FirstTDLoop.addData('ContinueTxt4.stopped', ContinueTxt4.tStopRefresh)
                # the Routine "SampleIntro" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "PlaySample"-------
                continueRoutine = True
                # update component parameters for each repeat
                EndPlay.keys = []
                EndPlay.rt = []
                _EndPlay_allKeys = []
                SyllableSound.setSound(TargetFile, hamming=True)
                SyllableSound.setVolume(1, log=False)
                Repeat.setSound(TargetFile, hamming=True)
                Repeat.setVolume(1, log=False)
                SoundTxt.setText(Target
)
                TrialNoTxt2.setText(TrialNo
)
                # keep track of which components have finished
                PlaySampleComponents = [EndPlay, SyllableSound, Repeat, SoundTxt, ContinueKey2, text_2, TrialNoTxt2]
                for thisComponent in PlaySampleComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                PlaySampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "PlaySample"-------
                while continueRoutine:
                    # get current time
                    t = PlaySampleClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=PlaySampleClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *EndPlay* updates
                    waitOnFlip = False
                    if EndPlay.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        EndPlay.frameNStart = frameN  # exact frame index
                        EndPlay.tStart = t  # local t and not account for scr refresh
                        EndPlay.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(EndPlay, 'tStartRefresh')  # time at next scr refresh
                        EndPlay.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(EndPlay.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(EndPlay.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if EndPlay.status == STARTED and not waitOnFlip:
                        theseKeys = EndPlay.getKeys(keyList=['space'], waitRelease=False)
                        _EndPlay_allKeys.extend(theseKeys)
                        if len(_EndPlay_allKeys):
                            EndPlay.keys = _EndPlay_allKeys[-1].name  # just the last key pressed
                            EndPlay.rt = _EndPlay_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    # start/stop SyllableSound
                    if SyllableSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        SyllableSound.frameNStart = frameN  # exact frame index
                        SyllableSound.tStart = t  # local t and not account for scr refresh
                        SyllableSound.tStartRefresh = tThisFlipGlobal  # on global time
                        SyllableSound.play(when=win)  # sync with win flip
                    # start/stop Repeat
                    if Repeat.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        Repeat.frameNStart = frameN  # exact frame index
                        Repeat.tStart = t  # local t and not account for scr refresh
                        Repeat.tStartRefresh = tThisFlipGlobal  # on global time
                        Repeat.play(when=win)  # sync with win flip
                    
                    # *SoundTxt* updates
                    if SoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        SoundTxt.frameNStart = frameN  # exact frame index
                        SoundTxt.tStart = t  # local t and not account for scr refresh
                        SoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(SoundTxt, 'tStartRefresh')  # time at next scr refresh
                        SoundTxt.setAutoDraw(True)
                    
                    # *ContinueKey2* updates
                    if ContinueKey2.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        ContinueKey2.frameNStart = frameN  # exact frame index
                        ContinueKey2.tStart = t  # local t and not account for scr refresh
                        ContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(ContinueKey2, 'tStartRefresh')  # time at next scr refresh
                        ContinueKey2.setAutoDraw(True)
                    
                    # *text_2* updates
                    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_2.frameNStart = frameN  # exact frame index
                        text_2.tStart = t  # local t and not account for scr refresh
                        text_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(True)
                    
                    # *TrialNoTxt2* updates
                    if TrialNoTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TrialNoTxt2.frameNStart = frameN  # exact frame index
                        TrialNoTxt2.tStart = t  # local t and not account for scr refresh
                        TrialNoTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TrialNoTxt2, 'tStartRefresh')  # time at next scr refresh
                        TrialNoTxt2.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in PlaySampleComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "PlaySample"-------
                for thisComponent in PlaySampleComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                SyllableSound.stop()  # ensure sound has stopped at end of routine
                FirstTDLoop.addData('SyllableSound.started', SyllableSound.tStartRefresh)
                FirstTDLoop.addData('SyllableSound.stopped', SyllableSound.tStopRefresh)
                Repeat.stop()  # ensure sound has stopped at end of routine
                FirstTDLoop.addData('Repeat.started', Repeat.tStartRefresh)
                FirstTDLoop.addData('Repeat.stopped', Repeat.tStopRefresh)
                FirstTDLoop.addData('SoundTxt.started', SoundTxt.tStartRefresh)
                FirstTDLoop.addData('SoundTxt.stopped', SoundTxt.tStopRefresh)
                FirstTDLoop.addData('ContinueKey2.started', ContinueKey2.tStartRefresh)
                FirstTDLoop.addData('ContinueKey2.stopped', ContinueKey2.tStopRefresh)
                FirstTDLoop.addData('text_2.started', text_2.tStartRefresh)
                FirstTDLoop.addData('text_2.stopped', text_2.tStopRefresh)
                FirstTDLoop.addData('TrialNoTxt2.started', TrialNoTxt2.tStartRefresh)
                FirstTDLoop.addData('TrialNoTxt2.stopped', TrialNoTxt2.tStopRefresh)
                # the Routine "PlaySample" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "TDStart"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                ## Randomize between 6 randomizations
                opt1 = "0:48" #FO #ta
                opt2 = "48:96" #FO #ta
                opt3 = "96:144" #FO #ta
                opt4 = "144:192" #KI #ta
                opt5 = "192:240" #KI #fe
                opt6 = "240:288" #KI
                opt7 = "288:336" #SI #re
                opt8 = "336:384" #SI
                opt9 = "384:432" #SI
                opt10 = "432:480" #TAY #ru
                opt11 = "480:528" #TAY
                opt12 = "528:576" #TAY
                
                if Target == "ru" or Target == "pu" or Target == "ni":
                    rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9])
                elif Target == "re" or Target == "ge" or Target == "me":
                    rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt10, opt11, opt12])
                elif Target == "fe" or Target == "ti" or Target == "su":
                    rows = random.choice([opt1, opt2, opt3, opt10, opt11, opt12, opt7, opt8, opt9])
                else:
                    rows = random.choice([opt10, opt11, opt12, opt4, opt5, opt6, opt7, opt8, opt9])
                # keep track of which components have finished
                TDStartComponents = [Countdown1]
                for thisComponent in TDStartComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                TDStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "TDStart"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = TDStartClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=TDStartClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *Countdown1* updates
                    if Countdown1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        Countdown1.frameNStart = frameN  # exact frame index
                        Countdown1.tStart = t  # local t and not account for scr refresh
                        Countdown1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Countdown1, 'tStartRefresh')  # time at next scr refresh
                        Countdown1.setAutoDraw(True)
                    if Countdown1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Countdown1.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            Countdown1.tStop = t  # not accounting for scr refresh
                            Countdown1.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(Countdown1, 'tStopRefresh')  # time at next scr refresh
                            Countdown1.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in TDStartComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "TDStart"-------
                for thisComponent in TDStartComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                FirstTDLoop.addData('Countdown1.started', Countdown1.tStartRefresh)
                FirstTDLoop.addData('Countdown1.stopped', Countdown1.tStopRefresh)
                
                # set up handler to look after randomisation of conditions etc
                FirstTD = data.TrialHandler(nReps=1, method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions(cond + "_TD_list.xlsx", selection=rows),
                    seed=None, name='FirstTD')
                thisExp.addLoop(FirstTD)  # add the loop to the experiment
                thisFirstTD = FirstTD.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisFirstTD.rgb)
                if thisFirstTD != None:
                    for paramName in thisFirstTD:
                        exec('{} = thisFirstTD[paramName]'.format(paramName))
                
                for thisFirstTD in FirstTD:
                    currentLoop = FirstTD
                    # abbreviate parameter names if possible (e.g. rgb = thisFirstTD.rgb)
                    if thisFirstTD != None:
                        for paramName in thisFirstTD:
                            exec('{} = thisFirstTD[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "trial_separate"-------
                    continueRoutine = True
                    # update component parameters for each repeat
                    if TDSound == Target:
                        TargetOnsetP = mytimerP.getTime()
                    soundOnsetP = mytimerP.getTime()
                    
                    
                    PlaySound.setSound(TDSoundFile, hamming=True)
                    PlaySound.setVolume(1, log=False)
                    PlayResp.keys = []
                    PlayResp.rt = []
                    _PlayResp_allKeys = []
                    TargetSoundTxt.setText(Target)
                    # keep track of which components have finished
                    trial_separateComponents = [PlaySound, PlayText, PlayResp, TargetSoundTxt]
                    for thisComponent in trial_separateComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    trial_separateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    
                    # -------Run Routine "trial_separate"-------
                    while continueRoutine:
                        # get current time
                        t = trial_separateClock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=trial_separateClock)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        # start/stop PlaySound
                        if PlaySound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            PlaySound.frameNStart = frameN  # exact frame index
                            PlaySound.tStart = t  # local t and not account for scr refresh
                            PlaySound.tStartRefresh = tThisFlipGlobal  # on global time
                            PlaySound.play(when=win)  # sync with win flip
                        
                        # *PlayText* updates
                        if PlayText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            PlayText.frameNStart = frameN  # exact frame index
                            PlayText.tStart = t  # local t and not account for scr refresh
                            PlayText.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(PlayText, 'tStartRefresh')  # time at next scr refresh
                            PlayText.setAutoDraw(True)
                        if PlayText.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > PlayText.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                PlayText.tStop = t  # not accounting for scr refresh
                                PlayText.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(PlayText, 'tStopRefresh')  # time at next scr refresh
                                PlayText.setAutoDraw(False)
                        
                        # *PlayResp* updates
                        waitOnFlip = False
                        if PlayResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            PlayResp.frameNStart = frameN  # exact frame index
                            PlayResp.tStart = t  # local t and not account for scr refresh
                            PlayResp.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(PlayResp, 'tStartRefresh')  # time at next scr refresh
                            PlayResp.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(PlayResp.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(PlayResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if PlayResp.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > PlayResp.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                PlayResp.tStop = t  # not accounting for scr refresh
                                PlayResp.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(PlayResp, 'tStopRefresh')  # time at next scr refresh
                                PlayResp.status = FINISHED
                        if PlayResp.status == STARTED and not waitOnFlip:
                            theseKeys = PlayResp.getKeys(keyList=['space'], waitRelease=False)
                            _PlayResp_allKeys.extend(theseKeys)
                            if len(_PlayResp_allKeys):
                                PlayResp.keys = [key.name for key in _PlayResp_allKeys]  # storing all keys
                                PlayResp.rt = [key.rt for key in _PlayResp_allKeys]
                        
                        # *TargetSoundTxt* updates
                        if TargetSoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            TargetSoundTxt.frameNStart = frameN  # exact frame index
                            TargetSoundTxt.tStart = t  # local t and not account for scr refresh
                            TargetSoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(TargetSoundTxt, 'tStartRefresh')  # time at next scr refresh
                            TargetSoundTxt.setAutoDraw(True)
                        if TargetSoundTxt.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > TargetSoundTxt.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                TargetSoundTxt.tStop = t  # not accounting for scr refresh
                                TargetSoundTxt.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(TargetSoundTxt, 'tStopRefresh')  # time at next scr refresh
                                TargetSoundTxt.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_separateComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "trial_separate"-------
                    for thisComponent in trial_separateComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # Set Target Onset time
                    TD.addData('TargetOnsetP', TargetOnsetP)
                    # Check if keyboard has been pressed
                    if PlayResp.keys in ['', [], None]:
                        PlayResp.keys = None
                    if PlayResp.keys != None: # we had a response
                        respcountP += 1
                        #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
                        respOnsetP = PlayResp.rt[0] + soundOnsetP    
                        # Check if the response is too close to the previous valid response
                        if respOnsetP - previousOnsetP > 1.2:
                            # Calculate RT
                            reactiontimeP = respOnsetP - TargetOnsetP
                            # Check if RT is below the cutoff
                            if reactiontimeP < 1.2:
                                TD.addData('ReactionTimeP', reactiontimeP)
                                TD.addData('TargetSyllable', Target)
                                TD.addData('TargetPosition', Position)
                                TD.addData('TargetOccurence', OccurenceC)
                                # Count it as a valid "hit"
                                hit += 1
                                # Use this as the latest valid response
                                previousOnsetP = respOnsetP
                    
                    PlaySound.stop()  # ensure sound has stopped at end of routine
                    FirstTD.addData('PlaySound.started', PlaySound.tStartRefresh)
                    FirstTD.addData('PlaySound.stopped', PlaySound.tStopRefresh)
                    FirstTD.addData('PlayText.started', PlayText.tStartRefresh)
                    FirstTD.addData('PlayText.stopped', PlayText.tStopRefresh)
                    # check responses
                    if PlayResp.keys in ['', [], None]:  # No response was made
                        PlayResp.keys = None
                    FirstTD.addData('PlayResp.keys',PlayResp.keys)
                    if PlayResp.keys != None:  # we had a response
                        FirstTD.addData('PlayResp.rt', PlayResp.rt)
                    FirstTD.addData('PlayResp.started', PlayResp.tStartRefresh)
                    FirstTD.addData('PlayResp.stopped', PlayResp.tStopRefresh)
                    FirstTD.addData('TargetSoundTxt.started', TargetSoundTxt.tStartRefresh)
                    FirstTD.addData('TargetSoundTxt.stopped', TargetSoundTxt.tStopRefresh)
                    # the Routine "trial_separate" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 1 repeats of 'FirstTD'
                
                
                # ------Prepare to start Routine "Pause1sec"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                # keep track of which components have finished
                Pause1secComponents = [PauseTxt2]
                for thisComponent in Pause1secComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                Pause1secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Pause1sec"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = Pause1secClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=Pause1secClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *PauseTxt2* updates
                    if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PauseTxt2.frameNStart = frameN  # exact frame index
                        PauseTxt2.tStart = t  # local t and not account for scr refresh
                        PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                        PauseTxt2.setAutoDraw(True)
                    if PauseTxt2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            PauseTxt2.tStop = t  # not accounting for scr refresh
                            PauseTxt2.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(PauseTxt2, 'tStopRefresh')  # time at next scr refresh
                            PauseTxt2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Pause1secComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Pause1sec"-------
                for thisComponent in Pause1secComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                FirstTDLoop.addData('PauseTxt2.started', PauseTxt2.tStartRefresh)
                FirstTDLoop.addData('PauseTxt2.stopped', PauseTxt2.tStopRefresh)
                
                # ------Prepare to start Routine "AddRespCountCode"-------
                continueRoutine = True
                # update component parameters for each repeat
                # keep track of which components have finished
                AddRespCountCodeComponents = []
                for thisComponent in AddRespCountCodeComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                AddRespCountCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "AddRespCountCode"-------
                while continueRoutine:
                    # get current time
                    t = AddRespCountCodeClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=AddRespCountCodeClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in AddRespCountCodeComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "AddRespCountCode"-------
                for thisComponent in AddRespCountCodeComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                falsealarm = 0
                hitrate = 0
                if hit != 0:
                    falsealarm = 1-(hit/respcountP)
                    hitrate = hit/4
                
                TD.addData("RespCountP", respcountP)
                TD.addData("FalseAlarmRate", falsealarm)
                TD.addData("HitRate", hitrate)
                hit = 0
                respcountP = 0
                # the Routine "AddRespCountCode" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'FirstTDLoop'
            
            
            # ------Prepare to start Routine "AttentionCheck3"-------
            continueRoutine = True
            # update component parameters for each repeat
            AttnCheck3ContKey.keys = []
            AttnCheck3ContKey.rt = []
            _AttnCheck3ContKey_allKeys = []
            AttnCheck3Resp.setText('\n ')
            # keep track of which components have finished
            AttentionCheck3Components = [AttnCheck3ContKey, AttnCheck3Txt, AttnCheck3Resp, AttnCheck3Cont]
            for thisComponent in AttentionCheck3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AttentionCheck3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AttentionCheck3"-------
            while continueRoutine:
                # get current time
                t = AttentionCheck3Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AttentionCheck3Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *AttnCheck3ContKey* updates
                waitOnFlip = False
                if AttnCheck3ContKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttnCheck3ContKey.frameNStart = frameN  # exact frame index
                    AttnCheck3ContKey.tStart = t  # local t and not account for scr refresh
                    AttnCheck3ContKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttnCheck3ContKey, 'tStartRefresh')  # time at next scr refresh
                    AttnCheck3ContKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(AttnCheck3ContKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(AttnCheck3ContKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if AttnCheck3ContKey.status == STARTED and not waitOnFlip:
                    theseKeys = AttnCheck3ContKey.getKeys(keyList=['return'], waitRelease=False)
                    _AttnCheck3ContKey_allKeys.extend(theseKeys)
                    if len(_AttnCheck3ContKey_allKeys):
                        AttnCheck3ContKey.keys = _AttnCheck3ContKey_allKeys[-1].name  # just the last key pressed
                        AttnCheck3ContKey.rt = _AttnCheck3ContKey_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *AttnCheck3Txt* updates
                if AttnCheck3Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttnCheck3Txt.frameNStart = frameN  # exact frame index
                    AttnCheck3Txt.tStart = t  # local t and not account for scr refresh
                    AttnCheck3Txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttnCheck3Txt, 'tStartRefresh')  # time at next scr refresh
                    AttnCheck3Txt.setAutoDraw(True)
                
                # *AttnCheck3Resp* updates
                if AttnCheck3Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttnCheck3Resp.frameNStart = frameN  # exact frame index
                    AttnCheck3Resp.tStart = t  # local t and not account for scr refresh
                    AttnCheck3Resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttnCheck3Resp, 'tStartRefresh')  # time at next scr refresh
                    AttnCheck3Resp.setAutoDraw(True)
                
                # *AttnCheck3Cont* updates
                if AttnCheck3Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttnCheck3Cont.frameNStart = frameN  # exact frame index
                    AttnCheck3Cont.tStart = t  # local t and not account for scr refresh
                    AttnCheck3Cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttnCheck3Cont, 'tStartRefresh')  # time at next scr refresh
                    AttnCheck3Cont.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AttentionCheck3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AttentionCheck3"-------
            for thisComponent in AttentionCheck3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if AttnCheck3ContKey.keys in ['', [], None]:  # No response was made
                AttnCheck3ContKey.keys = None
            TD.addData('AttnCheck3ContKey.keys',AttnCheck3ContKey.keys)
            if AttnCheck3ContKey.keys != None:  # we had a response
                TD.addData('AttnCheck3ContKey.rt', AttnCheck3ContKey.rt)
            TD.addData('AttnCheck3ContKey.started', AttnCheck3ContKey.tStartRefresh)
            TD.addData('AttnCheck3ContKey.stopped', AttnCheck3ContKey.tStopRefresh)
            TD.addData('AttnCheck3Txt.started', AttnCheck3Txt.tStartRefresh)
            TD.addData('AttnCheck3Txt.stopped', AttnCheck3Txt.tStopRefresh)
            TD.addData('AttnCheck3Resp.text',AttnCheck3Resp.text)
            AttnCheck3Resp.reset()
            TD.addData('AttnCheck3Resp.started', AttnCheck3Resp.tStartRefresh)
            TD.addData('AttnCheck3Resp.stopped', AttnCheck3Resp.tStopRefresh)
            TD.addData('AttnCheck3Cont.started', AttnCheck3Cont.tStartRefresh)
            TD.addData('AttnCheck3Cont.stopped', AttnCheck3Cont.tStopRefresh)
            OccurenceC += 1
            # the Routine "AttentionCheck3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            SecondTDLoop = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('TargetSyllables.xlsx', selection=second),
                seed=None, name='SecondTDLoop')
            thisExp.addLoop(SecondTDLoop)  # add the loop to the experiment
            thisSecondTDLoop = SecondTDLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisSecondTDLoop.rgb)
            if thisSecondTDLoop != None:
                for paramName in thisSecondTDLoop:
                    exec('{} = thisSecondTDLoop[paramName]'.format(paramName))
            
            for thisSecondTDLoop in SecondTDLoop:
                currentLoop = SecondTDLoop
                # abbreviate parameter names if possible (e.g. rgb = thisSecondTDLoop.rgb)
                if thisSecondTDLoop != None:
                    for paramName in thisSecondTDLoop:
                        exec('{} = thisSecondTDLoop[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "SampleIntro"-------
                continueRoutine = True
                # update component parameters for each repeat
                PlayTargetKey.keys = []
                PlayTargetKey.rt = []
                _PlayTargetKey_allKeys = []
                TargetTxt.setText(Target)
                repeatCount += 1
                TrialNo = "Recording " + str(repeatCount) + " of 36"
                TrialNoTxt.setText(TrialNo)
                # keep track of which components have finished
                SampleIntroComponents = [TargetMssg, PlayTargetKey, TargetTxt, TrialNoTxt, ContinueTxt4]
                for thisComponent in SampleIntroComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                SampleIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "SampleIntro"-------
                while continueRoutine:
                    # get current time
                    t = SampleIntroClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=SampleIntroClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *TargetMssg* updates
                    if TargetMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TargetMssg.frameNStart = frameN  # exact frame index
                        TargetMssg.tStart = t  # local t and not account for scr refresh
                        TargetMssg.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TargetMssg, 'tStartRefresh')  # time at next scr refresh
                        TargetMssg.setAutoDraw(True)
                    
                    # *PlayTargetKey* updates
                    waitOnFlip = False
                    if PlayTargetKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PlayTargetKey.frameNStart = frameN  # exact frame index
                        PlayTargetKey.tStart = t  # local t and not account for scr refresh
                        PlayTargetKey.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PlayTargetKey, 'tStartRefresh')  # time at next scr refresh
                        PlayTargetKey.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(PlayTargetKey.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(PlayTargetKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if PlayTargetKey.status == STARTED and not waitOnFlip:
                        theseKeys = PlayTargetKey.getKeys(keyList=['space'], waitRelease=False)
                        _PlayTargetKey_allKeys.extend(theseKeys)
                        if len(_PlayTargetKey_allKeys):
                            PlayTargetKey.keys = _PlayTargetKey_allKeys[-1].name  # just the last key pressed
                            PlayTargetKey.rt = _PlayTargetKey_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *TargetTxt* updates
                    if TargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TargetTxt.frameNStart = frameN  # exact frame index
                        TargetTxt.tStart = t  # local t and not account for scr refresh
                        TargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TargetTxt, 'tStartRefresh')  # time at next scr refresh
                        TargetTxt.setAutoDraw(True)
                    
                    # *TrialNoTxt* updates
                    if TrialNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TrialNoTxt.frameNStart = frameN  # exact frame index
                        TrialNoTxt.tStart = t  # local t and not account for scr refresh
                        TrialNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TrialNoTxt, 'tStartRefresh')  # time at next scr refresh
                        TrialNoTxt.setAutoDraw(True)
                    
                    # *ContinueTxt4* updates
                    if ContinueTxt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        ContinueTxt4.frameNStart = frameN  # exact frame index
                        ContinueTxt4.tStart = t  # local t and not account for scr refresh
                        ContinueTxt4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(ContinueTxt4, 'tStartRefresh')  # time at next scr refresh
                        ContinueTxt4.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in SampleIntroComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "SampleIntro"-------
                for thisComponent in SampleIntroComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                SecondTDLoop.addData('TargetMssg.started', TargetMssg.tStartRefresh)
                SecondTDLoop.addData('TargetMssg.stopped', TargetMssg.tStopRefresh)
                # check responses
                if PlayTargetKey.keys in ['', [], None]:  # No response was made
                    PlayTargetKey.keys = None
                SecondTDLoop.addData('PlayTargetKey.keys',PlayTargetKey.keys)
                if PlayTargetKey.keys != None:  # we had a response
                    SecondTDLoop.addData('PlayTargetKey.rt', PlayTargetKey.rt)
                SecondTDLoop.addData('PlayTargetKey.started', PlayTargetKey.tStartRefresh)
                SecondTDLoop.addData('PlayTargetKey.stopped', PlayTargetKey.tStopRefresh)
                SecondTDLoop.addData('TargetTxt.started', TargetTxt.tStartRefresh)
                SecondTDLoop.addData('TargetTxt.stopped', TargetTxt.tStopRefresh)
                SecondTDLoop.addData('TrialNoTxt.started', TrialNoTxt.tStartRefresh)
                SecondTDLoop.addData('TrialNoTxt.stopped', TrialNoTxt.tStopRefresh)
                SecondTDLoop.addData('ContinueTxt4.started', ContinueTxt4.tStartRefresh)
                SecondTDLoop.addData('ContinueTxt4.stopped', ContinueTxt4.tStopRefresh)
                # the Routine "SampleIntro" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "PlaySample"-------
                continueRoutine = True
                # update component parameters for each repeat
                EndPlay.keys = []
                EndPlay.rt = []
                _EndPlay_allKeys = []
                SyllableSound.setSound(TargetFile, hamming=True)
                SyllableSound.setVolume(1, log=False)
                Repeat.setSound(TargetFile, hamming=True)
                Repeat.setVolume(1, log=False)
                SoundTxt.setText(Target
)
                TrialNoTxt2.setText(TrialNo
)
                # keep track of which components have finished
                PlaySampleComponents = [EndPlay, SyllableSound, Repeat, SoundTxt, ContinueKey2, text_2, TrialNoTxt2]
                for thisComponent in PlaySampleComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                PlaySampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "PlaySample"-------
                while continueRoutine:
                    # get current time
                    t = PlaySampleClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=PlaySampleClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *EndPlay* updates
                    waitOnFlip = False
                    if EndPlay.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        EndPlay.frameNStart = frameN  # exact frame index
                        EndPlay.tStart = t  # local t and not account for scr refresh
                        EndPlay.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(EndPlay, 'tStartRefresh')  # time at next scr refresh
                        EndPlay.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(EndPlay.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(EndPlay.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if EndPlay.status == STARTED and not waitOnFlip:
                        theseKeys = EndPlay.getKeys(keyList=['space'], waitRelease=False)
                        _EndPlay_allKeys.extend(theseKeys)
                        if len(_EndPlay_allKeys):
                            EndPlay.keys = _EndPlay_allKeys[-1].name  # just the last key pressed
                            EndPlay.rt = _EndPlay_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    # start/stop SyllableSound
                    if SyllableSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        SyllableSound.frameNStart = frameN  # exact frame index
                        SyllableSound.tStart = t  # local t and not account for scr refresh
                        SyllableSound.tStartRefresh = tThisFlipGlobal  # on global time
                        SyllableSound.play(when=win)  # sync with win flip
                    # start/stop Repeat
                    if Repeat.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        Repeat.frameNStart = frameN  # exact frame index
                        Repeat.tStart = t  # local t and not account for scr refresh
                        Repeat.tStartRefresh = tThisFlipGlobal  # on global time
                        Repeat.play(when=win)  # sync with win flip
                    
                    # *SoundTxt* updates
                    if SoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        SoundTxt.frameNStart = frameN  # exact frame index
                        SoundTxt.tStart = t  # local t and not account for scr refresh
                        SoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(SoundTxt, 'tStartRefresh')  # time at next scr refresh
                        SoundTxt.setAutoDraw(True)
                    
                    # *ContinueKey2* updates
                    if ContinueKey2.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        ContinueKey2.frameNStart = frameN  # exact frame index
                        ContinueKey2.tStart = t  # local t and not account for scr refresh
                        ContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(ContinueKey2, 'tStartRefresh')  # time at next scr refresh
                        ContinueKey2.setAutoDraw(True)
                    
                    # *text_2* updates
                    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_2.frameNStart = frameN  # exact frame index
                        text_2.tStart = t  # local t and not account for scr refresh
                        text_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(True)
                    
                    # *TrialNoTxt2* updates
                    if TrialNoTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TrialNoTxt2.frameNStart = frameN  # exact frame index
                        TrialNoTxt2.tStart = t  # local t and not account for scr refresh
                        TrialNoTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TrialNoTxt2, 'tStartRefresh')  # time at next scr refresh
                        TrialNoTxt2.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in PlaySampleComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "PlaySample"-------
                for thisComponent in PlaySampleComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                SyllableSound.stop()  # ensure sound has stopped at end of routine
                SecondTDLoop.addData('SyllableSound.started', SyllableSound.tStartRefresh)
                SecondTDLoop.addData('SyllableSound.stopped', SyllableSound.tStopRefresh)
                Repeat.stop()  # ensure sound has stopped at end of routine
                SecondTDLoop.addData('Repeat.started', Repeat.tStartRefresh)
                SecondTDLoop.addData('Repeat.stopped', Repeat.tStopRefresh)
                SecondTDLoop.addData('SoundTxt.started', SoundTxt.tStartRefresh)
                SecondTDLoop.addData('SoundTxt.stopped', SoundTxt.tStopRefresh)
                SecondTDLoop.addData('ContinueKey2.started', ContinueKey2.tStartRefresh)
                SecondTDLoop.addData('ContinueKey2.stopped', ContinueKey2.tStopRefresh)
                SecondTDLoop.addData('text_2.started', text_2.tStartRefresh)
                SecondTDLoop.addData('text_2.stopped', text_2.tStopRefresh)
                SecondTDLoop.addData('TrialNoTxt2.started', TrialNoTxt2.tStartRefresh)
                SecondTDLoop.addData('TrialNoTxt2.stopped', TrialNoTxt2.tStopRefresh)
                # the Routine "PlaySample" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "TDStart"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                ## Randomize between 6 randomizations
                opt1 = "0:48" #FO #ta
                opt2 = "48:96" #FO #ta
                opt3 = "96:144" #FO #ta
                opt4 = "144:192" #KI #ta
                opt5 = "192:240" #KI #fe
                opt6 = "240:288" #KI
                opt7 = "288:336" #SI #re
                opt8 = "336:384" #SI
                opt9 = "384:432" #SI
                opt10 = "432:480" #TAY #ru
                opt11 = "480:528" #TAY
                opt12 = "528:576" #TAY
                
                if Target == "ru" or Target == "pu" or Target == "ni":
                    rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9])
                elif Target == "re" or Target == "ge" or Target == "me":
                    rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt10, opt11, opt12])
                elif Target == "fe" or Target == "ti" or Target == "su":
                    rows = random.choice([opt1, opt2, opt3, opt10, opt11, opt12, opt7, opt8, opt9])
                else:
                    rows = random.choice([opt10, opt11, opt12, opt4, opt5, opt6, opt7, opt8, opt9])
                # keep track of which components have finished
                TDStartComponents = [Countdown1]
                for thisComponent in TDStartComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                TDStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "TDStart"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = TDStartClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=TDStartClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *Countdown1* updates
                    if Countdown1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        Countdown1.frameNStart = frameN  # exact frame index
                        Countdown1.tStart = t  # local t and not account for scr refresh
                        Countdown1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Countdown1, 'tStartRefresh')  # time at next scr refresh
                        Countdown1.setAutoDraw(True)
                    if Countdown1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Countdown1.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            Countdown1.tStop = t  # not accounting for scr refresh
                            Countdown1.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(Countdown1, 'tStopRefresh')  # time at next scr refresh
                            Countdown1.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in TDStartComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "TDStart"-------
                for thisComponent in TDStartComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                SecondTDLoop.addData('Countdown1.started', Countdown1.tStartRefresh)
                SecondTDLoop.addData('Countdown1.stopped', Countdown1.tStopRefresh)
                
                # set up handler to look after randomisation of conditions etc
                SecondTD = data.TrialHandler(nReps=1, method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions(cond+ "_TD_list.xlsx", selection=rows),
                    seed=None, name='SecondTD')
                thisExp.addLoop(SecondTD)  # add the loop to the experiment
                thisSecondTD = SecondTD.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisSecondTD.rgb)
                if thisSecondTD != None:
                    for paramName in thisSecondTD:
                        exec('{} = thisSecondTD[paramName]'.format(paramName))
                
                for thisSecondTD in SecondTD:
                    currentLoop = SecondTD
                    # abbreviate parameter names if possible (e.g. rgb = thisSecondTD.rgb)
                    if thisSecondTD != None:
                        for paramName in thisSecondTD:
                            exec('{} = thisSecondTD[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "trial_separate"-------
                    continueRoutine = True
                    # update component parameters for each repeat
                    if TDSound == Target:
                        TargetOnsetP = mytimerP.getTime()
                    soundOnsetP = mytimerP.getTime()
                    
                    
                    PlaySound.setSound(TDSoundFile, hamming=True)
                    PlaySound.setVolume(1, log=False)
                    PlayResp.keys = []
                    PlayResp.rt = []
                    _PlayResp_allKeys = []
                    TargetSoundTxt.setText(Target)
                    # keep track of which components have finished
                    trial_separateComponents = [PlaySound, PlayText, PlayResp, TargetSoundTxt]
                    for thisComponent in trial_separateComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    trial_separateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    
                    # -------Run Routine "trial_separate"-------
                    while continueRoutine:
                        # get current time
                        t = trial_separateClock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=trial_separateClock)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        # start/stop PlaySound
                        if PlaySound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            PlaySound.frameNStart = frameN  # exact frame index
                            PlaySound.tStart = t  # local t and not account for scr refresh
                            PlaySound.tStartRefresh = tThisFlipGlobal  # on global time
                            PlaySound.play(when=win)  # sync with win flip
                        
                        # *PlayText* updates
                        if PlayText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            PlayText.frameNStart = frameN  # exact frame index
                            PlayText.tStart = t  # local t and not account for scr refresh
                            PlayText.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(PlayText, 'tStartRefresh')  # time at next scr refresh
                            PlayText.setAutoDraw(True)
                        if PlayText.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > PlayText.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                PlayText.tStop = t  # not accounting for scr refresh
                                PlayText.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(PlayText, 'tStopRefresh')  # time at next scr refresh
                                PlayText.setAutoDraw(False)
                        
                        # *PlayResp* updates
                        waitOnFlip = False
                        if PlayResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            PlayResp.frameNStart = frameN  # exact frame index
                            PlayResp.tStart = t  # local t and not account for scr refresh
                            PlayResp.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(PlayResp, 'tStartRefresh')  # time at next scr refresh
                            PlayResp.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(PlayResp.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(PlayResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if PlayResp.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > PlayResp.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                PlayResp.tStop = t  # not accounting for scr refresh
                                PlayResp.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(PlayResp, 'tStopRefresh')  # time at next scr refresh
                                PlayResp.status = FINISHED
                        if PlayResp.status == STARTED and not waitOnFlip:
                            theseKeys = PlayResp.getKeys(keyList=['space'], waitRelease=False)
                            _PlayResp_allKeys.extend(theseKeys)
                            if len(_PlayResp_allKeys):
                                PlayResp.keys = [key.name for key in _PlayResp_allKeys]  # storing all keys
                                PlayResp.rt = [key.rt for key in _PlayResp_allKeys]
                        
                        # *TargetSoundTxt* updates
                        if TargetSoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            TargetSoundTxt.frameNStart = frameN  # exact frame index
                            TargetSoundTxt.tStart = t  # local t and not account for scr refresh
                            TargetSoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(TargetSoundTxt, 'tStartRefresh')  # time at next scr refresh
                            TargetSoundTxt.setAutoDraw(True)
                        if TargetSoundTxt.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > TargetSoundTxt.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                TargetSoundTxt.tStop = t  # not accounting for scr refresh
                                TargetSoundTxt.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(TargetSoundTxt, 'tStopRefresh')  # time at next scr refresh
                                TargetSoundTxt.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_separateComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "trial_separate"-------
                    for thisComponent in trial_separateComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # Set Target Onset time
                    TD.addData('TargetOnsetP', TargetOnsetP)
                    # Check if keyboard has been pressed
                    if PlayResp.keys in ['', [], None]:
                        PlayResp.keys = None
                    if PlayResp.keys != None: # we had a response
                        respcountP += 1
                        #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
                        respOnsetP = PlayResp.rt[0] + soundOnsetP    
                        # Check if the response is too close to the previous valid response
                        if respOnsetP - previousOnsetP > 1.2:
                            # Calculate RT
                            reactiontimeP = respOnsetP - TargetOnsetP
                            # Check if RT is below the cutoff
                            if reactiontimeP < 1.2:
                                TD.addData('ReactionTimeP', reactiontimeP)
                                TD.addData('TargetSyllable', Target)
                                TD.addData('TargetPosition', Position)
                                TD.addData('TargetOccurence', OccurenceC)
                                # Count it as a valid "hit"
                                hit += 1
                                # Use this as the latest valid response
                                previousOnsetP = respOnsetP
                    
                    PlaySound.stop()  # ensure sound has stopped at end of routine
                    SecondTD.addData('PlaySound.started', PlaySound.tStartRefresh)
                    SecondTD.addData('PlaySound.stopped', PlaySound.tStopRefresh)
                    SecondTD.addData('PlayText.started', PlayText.tStartRefresh)
                    SecondTD.addData('PlayText.stopped', PlayText.tStopRefresh)
                    # check responses
                    if PlayResp.keys in ['', [], None]:  # No response was made
                        PlayResp.keys = None
                    SecondTD.addData('PlayResp.keys',PlayResp.keys)
                    if PlayResp.keys != None:  # we had a response
                        SecondTD.addData('PlayResp.rt', PlayResp.rt)
                    SecondTD.addData('PlayResp.started', PlayResp.tStartRefresh)
                    SecondTD.addData('PlayResp.stopped', PlayResp.tStopRefresh)
                    SecondTD.addData('TargetSoundTxt.started', TargetSoundTxt.tStartRefresh)
                    SecondTD.addData('TargetSoundTxt.stopped', TargetSoundTxt.tStopRefresh)
                    # the Routine "trial_separate" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 1 repeats of 'SecondTD'
                
                
                # ------Prepare to start Routine "Pause1sec"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                # keep track of which components have finished
                Pause1secComponents = [PauseTxt2]
                for thisComponent in Pause1secComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                Pause1secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Pause1sec"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = Pause1secClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=Pause1secClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *PauseTxt2* updates
                    if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PauseTxt2.frameNStart = frameN  # exact frame index
                        PauseTxt2.tStart = t  # local t and not account for scr refresh
                        PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                        PauseTxt2.setAutoDraw(True)
                    if PauseTxt2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            PauseTxt2.tStop = t  # not accounting for scr refresh
                            PauseTxt2.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(PauseTxt2, 'tStopRefresh')  # time at next scr refresh
                            PauseTxt2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Pause1secComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Pause1sec"-------
                for thisComponent in Pause1secComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                SecondTDLoop.addData('PauseTxt2.started', PauseTxt2.tStartRefresh)
                SecondTDLoop.addData('PauseTxt2.stopped', PauseTxt2.tStopRefresh)
                
                # ------Prepare to start Routine "AddRespCountCode"-------
                continueRoutine = True
                # update component parameters for each repeat
                # keep track of which components have finished
                AddRespCountCodeComponents = []
                for thisComponent in AddRespCountCodeComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                AddRespCountCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "AddRespCountCode"-------
                while continueRoutine:
                    # get current time
                    t = AddRespCountCodeClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=AddRespCountCodeClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in AddRespCountCodeComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "AddRespCountCode"-------
                for thisComponent in AddRespCountCodeComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                falsealarm = 0
                hitrate = 0
                if hit != 0:
                    falsealarm = 1-(hit/respcountP)
                    hitrate = hit/4
                
                TD.addData("RespCountP", respcountP)
                TD.addData("FalseAlarmRate", falsealarm)
                TD.addData("HitRate", hitrate)
                hit = 0
                respcountP = 0
                # the Routine "AddRespCountCode" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'SecondTDLoop'
            
            
            # ------Prepare to start Routine "AttentionCheck1"-------
            continueRoutine = True
            # update component parameters for each repeat
            AttentionKey1.keys = []
            AttentionKey1.rt = []
            _AttentionKey1_allKeys = []
            AttnCheck1Resp.setText('\n ')
            # keep track of which components have finished
            AttentionCheck1Components = [AttentionKey1, AttentionCheck1Txt, AttnCheck1Resp, AttnCheck1Cont]
            for thisComponent in AttentionCheck1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AttentionCheck1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AttentionCheck1"-------
            while continueRoutine:
                # get current time
                t = AttentionCheck1Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AttentionCheck1Clock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *AttentionKey1* updates
                waitOnFlip = False
                if AttentionKey1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttentionKey1.frameNStart = frameN  # exact frame index
                    AttentionKey1.tStart = t  # local t and not account for scr refresh
                    AttentionKey1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttentionKey1, 'tStartRefresh')  # time at next scr refresh
                    AttentionKey1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(AttentionKey1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(AttentionKey1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if AttentionKey1.status == STARTED and not waitOnFlip:
                    theseKeys = AttentionKey1.getKeys(keyList=['1', '2', 'return'], waitRelease=False)
                    _AttentionKey1_allKeys.extend(theseKeys)
                    if len(_AttentionKey1_allKeys):
                        AttentionKey1.keys = _AttentionKey1_allKeys[-1].name  # just the last key pressed
                        AttentionKey1.rt = _AttentionKey1_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *AttentionCheck1Txt* updates
                if AttentionCheck1Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttentionCheck1Txt.frameNStart = frameN  # exact frame index
                    AttentionCheck1Txt.tStart = t  # local t and not account for scr refresh
                    AttentionCheck1Txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttentionCheck1Txt, 'tStartRefresh')  # time at next scr refresh
                    AttentionCheck1Txt.setAutoDraw(True)
                
                # *AttnCheck1Resp* updates
                if AttnCheck1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttnCheck1Resp.frameNStart = frameN  # exact frame index
                    AttnCheck1Resp.tStart = t  # local t and not account for scr refresh
                    AttnCheck1Resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttnCheck1Resp, 'tStartRefresh')  # time at next scr refresh
                    AttnCheck1Resp.setAutoDraw(True)
                
                # *AttnCheck1Cont* updates
                if AttnCheck1Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AttnCheck1Cont.frameNStart = frameN  # exact frame index
                    AttnCheck1Cont.tStart = t  # local t and not account for scr refresh
                    AttnCheck1Cont.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttnCheck1Cont, 'tStartRefresh')  # time at next scr refresh
                    AttnCheck1Cont.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AttentionCheck1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AttentionCheck1"-------
            for thisComponent in AttentionCheck1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if AttentionKey1.keys in ['', [], None]:  # No response was made
                AttentionKey1.keys = None
            TD.addData('AttentionKey1.keys',AttentionKey1.keys)
            if AttentionKey1.keys != None:  # we had a response
                TD.addData('AttentionKey1.rt', AttentionKey1.rt)
            TD.addData('AttentionKey1.started', AttentionKey1.tStartRefresh)
            TD.addData('AttentionKey1.stopped', AttentionKey1.tStopRefresh)
            TD.addData('AttentionCheck1Txt.started', AttentionCheck1Txt.tStartRefresh)
            TD.addData('AttentionCheck1Txt.stopped', AttentionCheck1Txt.tStopRefresh)
            TD.addData('AttnCheck1Resp.text',AttnCheck1Resp.text)
            AttnCheck1Resp.reset()
            TD.addData('AttnCheck1Resp.started', AttnCheck1Resp.tStartRefresh)
            TD.addData('AttnCheck1Resp.stopped', AttnCheck1Resp.tStopRefresh)
            TD.addData('AttnCheck1Cont.started', AttnCheck1Cont.tStartRefresh)
            TD.addData('AttnCheck1Cont.stopped', AttnCheck1Cont.tStopRefresh)
            OccurenceC += 1
            # the Routine "AttentionCheck1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            thirdTDLoop = data.TrialHandler(nReps=1, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('TargetSyllables.xlsx', selection=third),
                seed=None, name='thirdTDLoop')
            thisExp.addLoop(thirdTDLoop)  # add the loop to the experiment
            thisThirdTDLoop = thirdTDLoop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisThirdTDLoop.rgb)
            if thisThirdTDLoop != None:
                for paramName in thisThirdTDLoop:
                    exec('{} = thisThirdTDLoop[paramName]'.format(paramName))
            
            for thisThirdTDLoop in thirdTDLoop:
                currentLoop = thirdTDLoop
                # abbreviate parameter names if possible (e.g. rgb = thisThirdTDLoop.rgb)
                if thisThirdTDLoop != None:
                    for paramName in thisThirdTDLoop:
                        exec('{} = thisThirdTDLoop[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "SampleIntro"-------
                continueRoutine = True
                # update component parameters for each repeat
                PlayTargetKey.keys = []
                PlayTargetKey.rt = []
                _PlayTargetKey_allKeys = []
                TargetTxt.setText(Target)
                repeatCount += 1
                TrialNo = "Recording " + str(repeatCount) + " of 36"
                TrialNoTxt.setText(TrialNo)
                # keep track of which components have finished
                SampleIntroComponents = [TargetMssg, PlayTargetKey, TargetTxt, TrialNoTxt, ContinueTxt4]
                for thisComponent in SampleIntroComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                SampleIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "SampleIntro"-------
                while continueRoutine:
                    # get current time
                    t = SampleIntroClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=SampleIntroClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *TargetMssg* updates
                    if TargetMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TargetMssg.frameNStart = frameN  # exact frame index
                        TargetMssg.tStart = t  # local t and not account for scr refresh
                        TargetMssg.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TargetMssg, 'tStartRefresh')  # time at next scr refresh
                        TargetMssg.setAutoDraw(True)
                    
                    # *PlayTargetKey* updates
                    waitOnFlip = False
                    if PlayTargetKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PlayTargetKey.frameNStart = frameN  # exact frame index
                        PlayTargetKey.tStart = t  # local t and not account for scr refresh
                        PlayTargetKey.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PlayTargetKey, 'tStartRefresh')  # time at next scr refresh
                        PlayTargetKey.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(PlayTargetKey.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(PlayTargetKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if PlayTargetKey.status == STARTED and not waitOnFlip:
                        theseKeys = PlayTargetKey.getKeys(keyList=['space'], waitRelease=False)
                        _PlayTargetKey_allKeys.extend(theseKeys)
                        if len(_PlayTargetKey_allKeys):
                            PlayTargetKey.keys = _PlayTargetKey_allKeys[-1].name  # just the last key pressed
                            PlayTargetKey.rt = _PlayTargetKey_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *TargetTxt* updates
                    if TargetTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TargetTxt.frameNStart = frameN  # exact frame index
                        TargetTxt.tStart = t  # local t and not account for scr refresh
                        TargetTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TargetTxt, 'tStartRefresh')  # time at next scr refresh
                        TargetTxt.setAutoDraw(True)
                    
                    # *TrialNoTxt* updates
                    if TrialNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TrialNoTxt.frameNStart = frameN  # exact frame index
                        TrialNoTxt.tStart = t  # local t and not account for scr refresh
                        TrialNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TrialNoTxt, 'tStartRefresh')  # time at next scr refresh
                        TrialNoTxt.setAutoDraw(True)
                    
                    # *ContinueTxt4* updates
                    if ContinueTxt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        ContinueTxt4.frameNStart = frameN  # exact frame index
                        ContinueTxt4.tStart = t  # local t and not account for scr refresh
                        ContinueTxt4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(ContinueTxt4, 'tStartRefresh')  # time at next scr refresh
                        ContinueTxt4.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in SampleIntroComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "SampleIntro"-------
                for thisComponent in SampleIntroComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thirdTDLoop.addData('TargetMssg.started', TargetMssg.tStartRefresh)
                thirdTDLoop.addData('TargetMssg.stopped', TargetMssg.tStopRefresh)
                # check responses
                if PlayTargetKey.keys in ['', [], None]:  # No response was made
                    PlayTargetKey.keys = None
                thirdTDLoop.addData('PlayTargetKey.keys',PlayTargetKey.keys)
                if PlayTargetKey.keys != None:  # we had a response
                    thirdTDLoop.addData('PlayTargetKey.rt', PlayTargetKey.rt)
                thirdTDLoop.addData('PlayTargetKey.started', PlayTargetKey.tStartRefresh)
                thirdTDLoop.addData('PlayTargetKey.stopped', PlayTargetKey.tStopRefresh)
                thirdTDLoop.addData('TargetTxt.started', TargetTxt.tStartRefresh)
                thirdTDLoop.addData('TargetTxt.stopped', TargetTxt.tStopRefresh)
                thirdTDLoop.addData('TrialNoTxt.started', TrialNoTxt.tStartRefresh)
                thirdTDLoop.addData('TrialNoTxt.stopped', TrialNoTxt.tStopRefresh)
                thirdTDLoop.addData('ContinueTxt4.started', ContinueTxt4.tStartRefresh)
                thirdTDLoop.addData('ContinueTxt4.stopped', ContinueTxt4.tStopRefresh)
                # the Routine "SampleIntro" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "PlaySample"-------
                continueRoutine = True
                # update component parameters for each repeat
                EndPlay.keys = []
                EndPlay.rt = []
                _EndPlay_allKeys = []
                SyllableSound.setSound(TargetFile, hamming=True)
                SyllableSound.setVolume(1, log=False)
                Repeat.setSound(TargetFile, hamming=True)
                Repeat.setVolume(1, log=False)
                SoundTxt.setText(Target
)
                TrialNoTxt2.setText(TrialNo
)
                # keep track of which components have finished
                PlaySampleComponents = [EndPlay, SyllableSound, Repeat, SoundTxt, ContinueKey2, text_2, TrialNoTxt2]
                for thisComponent in PlaySampleComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                PlaySampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "PlaySample"-------
                while continueRoutine:
                    # get current time
                    t = PlaySampleClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=PlaySampleClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *EndPlay* updates
                    waitOnFlip = False
                    if EndPlay.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        EndPlay.frameNStart = frameN  # exact frame index
                        EndPlay.tStart = t  # local t and not account for scr refresh
                        EndPlay.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(EndPlay, 'tStartRefresh')  # time at next scr refresh
                        EndPlay.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(EndPlay.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(EndPlay.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if EndPlay.status == STARTED and not waitOnFlip:
                        theseKeys = EndPlay.getKeys(keyList=['space'], waitRelease=False)
                        _EndPlay_allKeys.extend(theseKeys)
                        if len(_EndPlay_allKeys):
                            EndPlay.keys = _EndPlay_allKeys[-1].name  # just the last key pressed
                            EndPlay.rt = _EndPlay_allKeys[-1].rt
                            # a response ends the routine
                            continueRoutine = False
                    # start/stop SyllableSound
                    if SyllableSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        SyllableSound.frameNStart = frameN  # exact frame index
                        SyllableSound.tStart = t  # local t and not account for scr refresh
                        SyllableSound.tStartRefresh = tThisFlipGlobal  # on global time
                        SyllableSound.play(when=win)  # sync with win flip
                    # start/stop Repeat
                    if Repeat.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        Repeat.frameNStart = frameN  # exact frame index
                        Repeat.tStart = t  # local t and not account for scr refresh
                        Repeat.tStartRefresh = tThisFlipGlobal  # on global time
                        Repeat.play(when=win)  # sync with win flip
                    
                    # *SoundTxt* updates
                    if SoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        SoundTxt.frameNStart = frameN  # exact frame index
                        SoundTxt.tStart = t  # local t and not account for scr refresh
                        SoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(SoundTxt, 'tStartRefresh')  # time at next scr refresh
                        SoundTxt.setAutoDraw(True)
                    
                    # *ContinueKey2* updates
                    if ContinueKey2.status == NOT_STARTED and tThisFlip >= SyllableSound.getDuration() + 1-frameTolerance:
                        # keep track of start time/frame for later
                        ContinueKey2.frameNStart = frameN  # exact frame index
                        ContinueKey2.tStart = t  # local t and not account for scr refresh
                        ContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(ContinueKey2, 'tStartRefresh')  # time at next scr refresh
                        ContinueKey2.setAutoDraw(True)
                    
                    # *text_2* updates
                    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_2.frameNStart = frameN  # exact frame index
                        text_2.tStart = t  # local t and not account for scr refresh
                        text_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                        text_2.setAutoDraw(True)
                    
                    # *TrialNoTxt2* updates
                    if TrialNoTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        TrialNoTxt2.frameNStart = frameN  # exact frame index
                        TrialNoTxt2.tStart = t  # local t and not account for scr refresh
                        TrialNoTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(TrialNoTxt2, 'tStartRefresh')  # time at next scr refresh
                        TrialNoTxt2.setAutoDraw(True)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in PlaySampleComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "PlaySample"-------
                for thisComponent in PlaySampleComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                SyllableSound.stop()  # ensure sound has stopped at end of routine
                thirdTDLoop.addData('SyllableSound.started', SyllableSound.tStartRefresh)
                thirdTDLoop.addData('SyllableSound.stopped', SyllableSound.tStopRefresh)
                Repeat.stop()  # ensure sound has stopped at end of routine
                thirdTDLoop.addData('Repeat.started', Repeat.tStartRefresh)
                thirdTDLoop.addData('Repeat.stopped', Repeat.tStopRefresh)
                thirdTDLoop.addData('SoundTxt.started', SoundTxt.tStartRefresh)
                thirdTDLoop.addData('SoundTxt.stopped', SoundTxt.tStopRefresh)
                thirdTDLoop.addData('ContinueKey2.started', ContinueKey2.tStartRefresh)
                thirdTDLoop.addData('ContinueKey2.stopped', ContinueKey2.tStopRefresh)
                thirdTDLoop.addData('text_2.started', text_2.tStartRefresh)
                thirdTDLoop.addData('text_2.stopped', text_2.tStopRefresh)
                thirdTDLoop.addData('TrialNoTxt2.started', TrialNoTxt2.tStartRefresh)
                thirdTDLoop.addData('TrialNoTxt2.stopped', TrialNoTxt2.tStopRefresh)
                # the Routine "PlaySample" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # ------Prepare to start Routine "TDStart"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                ## Randomize between 6 randomizations
                opt1 = "0:48" #FO #ta
                opt2 = "48:96" #FO #ta
                opt3 = "96:144" #FO #ta
                opt4 = "144:192" #KI #ta
                opt5 = "192:240" #KI #fe
                opt6 = "240:288" #KI
                opt7 = "288:336" #SI #re
                opt8 = "336:384" #SI
                opt9 = "384:432" #SI
                opt10 = "432:480" #TAY #ru
                opt11 = "480:528" #TAY
                opt12 = "528:576" #TAY
                
                if Target == "ru" or Target == "pu" or Target == "ni":
                    rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9])
                elif Target == "re" or Target == "ge" or Target == "me":
                    rows = random.choice([opt1, opt2, opt3, opt4, opt5, opt6, opt10, opt11, opt12])
                elif Target == "fe" or Target == "ti" or Target == "su":
                    rows = random.choice([opt1, opt2, opt3, opt10, opt11, opt12, opt7, opt8, opt9])
                else:
                    rows = random.choice([opt10, opt11, opt12, opt4, opt5, opt6, opt7, opt8, opt9])
                # keep track of which components have finished
                TDStartComponents = [Countdown1]
                for thisComponent in TDStartComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                TDStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "TDStart"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = TDStartClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=TDStartClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *Countdown1* updates
                    if Countdown1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        Countdown1.frameNStart = frameN  # exact frame index
                        Countdown1.tStart = t  # local t and not account for scr refresh
                        Countdown1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Countdown1, 'tStartRefresh')  # time at next scr refresh
                        Countdown1.setAutoDraw(True)
                    if Countdown1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Countdown1.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            Countdown1.tStop = t  # not accounting for scr refresh
                            Countdown1.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(Countdown1, 'tStopRefresh')  # time at next scr refresh
                            Countdown1.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in TDStartComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "TDStart"-------
                for thisComponent in TDStartComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thirdTDLoop.addData('Countdown1.started', Countdown1.tStartRefresh)
                thirdTDLoop.addData('Countdown1.stopped', Countdown1.tStopRefresh)
                
                # set up handler to look after randomisation of conditions etc
                ThirdTD = data.TrialHandler(nReps=1, method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions(cond + "_TD_list.xlsx", selection=rows),
                    seed=None, name='ThirdTD')
                thisExp.addLoop(ThirdTD)  # add the loop to the experiment
                thisThirdTD = ThirdTD.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisThirdTD.rgb)
                if thisThirdTD != None:
                    for paramName in thisThirdTD:
                        exec('{} = thisThirdTD[paramName]'.format(paramName))
                
                for thisThirdTD in ThirdTD:
                    currentLoop = ThirdTD
                    # abbreviate parameter names if possible (e.g. rgb = thisThirdTD.rgb)
                    if thisThirdTD != None:
                        for paramName in thisThirdTD:
                            exec('{} = thisThirdTD[paramName]'.format(paramName))
                    
                    # ------Prepare to start Routine "trial_separate"-------
                    continueRoutine = True
                    # update component parameters for each repeat
                    if TDSound == Target:
                        TargetOnsetP = mytimerP.getTime()
                    soundOnsetP = mytimerP.getTime()
                    
                    
                    PlaySound.setSound(TDSoundFile, hamming=True)
                    PlaySound.setVolume(1, log=False)
                    PlayResp.keys = []
                    PlayResp.rt = []
                    _PlayResp_allKeys = []
                    TargetSoundTxt.setText(Target)
                    # keep track of which components have finished
                    trial_separateComponents = [PlaySound, PlayText, PlayResp, TargetSoundTxt]
                    for thisComponent in trial_separateComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    trial_separateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                    frameN = -1
                    
                    # -------Run Routine "trial_separate"-------
                    while continueRoutine:
                        # get current time
                        t = trial_separateClock.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=trial_separateClock)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        # start/stop PlaySound
                        if PlaySound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            PlaySound.frameNStart = frameN  # exact frame index
                            PlaySound.tStart = t  # local t and not account for scr refresh
                            PlaySound.tStartRefresh = tThisFlipGlobal  # on global time
                            PlaySound.play(when=win)  # sync with win flip
                        
                        # *PlayText* updates
                        if PlayText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                            # keep track of start time/frame for later
                            PlayText.frameNStart = frameN  # exact frame index
                            PlayText.tStart = t  # local t and not account for scr refresh
                            PlayText.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(PlayText, 'tStartRefresh')  # time at next scr refresh
                            PlayText.setAutoDraw(True)
                        if PlayText.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > PlayText.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                PlayText.tStop = t  # not accounting for scr refresh
                                PlayText.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(PlayText, 'tStopRefresh')  # time at next scr refresh
                                PlayText.setAutoDraw(False)
                        
                        # *PlayResp* updates
                        waitOnFlip = False
                        if PlayResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            PlayResp.frameNStart = frameN  # exact frame index
                            PlayResp.tStart = t  # local t and not account for scr refresh
                            PlayResp.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(PlayResp, 'tStartRefresh')  # time at next scr refresh
                            PlayResp.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(PlayResp.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(PlayResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if PlayResp.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > PlayResp.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                PlayResp.tStop = t  # not accounting for scr refresh
                                PlayResp.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(PlayResp, 'tStopRefresh')  # time at next scr refresh
                                PlayResp.status = FINISHED
                        if PlayResp.status == STARTED and not waitOnFlip:
                            theseKeys = PlayResp.getKeys(keyList=['space'], waitRelease=False)
                            _PlayResp_allKeys.extend(theseKeys)
                            if len(_PlayResp_allKeys):
                                PlayResp.keys = [key.name for key in _PlayResp_allKeys]  # storing all keys
                                PlayResp.rt = [key.rt for key in _PlayResp_allKeys]
                        
                        # *TargetSoundTxt* updates
                        if TargetSoundTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            TargetSoundTxt.frameNStart = frameN  # exact frame index
                            TargetSoundTxt.tStart = t  # local t and not account for scr refresh
                            TargetSoundTxt.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(TargetSoundTxt, 'tStartRefresh')  # time at next scr refresh
                            TargetSoundTxt.setAutoDraw(True)
                        if TargetSoundTxt.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > TargetSoundTxt.tStartRefresh + 0.38-frameTolerance:
                                # keep track of stop time/frame for later
                                TargetSoundTxt.tStop = t  # not accounting for scr refresh
                                TargetSoundTxt.frameNStop = frameN  # exact frame index
                                win.timeOnFlip(TargetSoundTxt, 'tStopRefresh')  # time at next scr refresh
                                TargetSoundTxt.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                            core.quit()
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_separateComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # -------Ending Routine "trial_separate"-------
                    for thisComponent in trial_separateComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # Set Target Onset time
                    TD.addData('TargetOnsetP', TargetOnsetP)
                    # Check if keyboard has been pressed
                    if PlayResp.keys in ['', [], None]:
                        PlayResp.keys = None
                    if PlayResp.keys != None: # we had a response
                        respcountP += 1
                        #respOnset = TrainResp.rt[0] + TDTrainSound.tStartRefresh
                        respOnsetP = PlayResp.rt[0] + soundOnsetP    
                        # Check if the response is too close to the previous valid response
                        if respOnsetP - previousOnsetP > 1.2:
                            # Calculate RT
                            reactiontimeP = respOnsetP - TargetOnsetP
                            # Check if RT is below the cutoff
                            if reactiontimeP < 1.2:
                                TD.addData('ReactionTimeP', reactiontimeP)
                                TD.addData('TargetSyllable', Target)
                                TD.addData('TargetPosition', Position)
                                TD.addData('TargetOccurence', OccurenceC)
                                # Count it as a valid "hit"
                                hit += 1
                                # Use this as the latest valid response
                                previousOnsetP = respOnsetP
                    
                    PlaySound.stop()  # ensure sound has stopped at end of routine
                    ThirdTD.addData('PlaySound.started', PlaySound.tStartRefresh)
                    ThirdTD.addData('PlaySound.stopped', PlaySound.tStopRefresh)
                    ThirdTD.addData('PlayText.started', PlayText.tStartRefresh)
                    ThirdTD.addData('PlayText.stopped', PlayText.tStopRefresh)
                    # check responses
                    if PlayResp.keys in ['', [], None]:  # No response was made
                        PlayResp.keys = None
                    ThirdTD.addData('PlayResp.keys',PlayResp.keys)
                    if PlayResp.keys != None:  # we had a response
                        ThirdTD.addData('PlayResp.rt', PlayResp.rt)
                    ThirdTD.addData('PlayResp.started', PlayResp.tStartRefresh)
                    ThirdTD.addData('PlayResp.stopped', PlayResp.tStopRefresh)
                    ThirdTD.addData('TargetSoundTxt.started', TargetSoundTxt.tStartRefresh)
                    ThirdTD.addData('TargetSoundTxt.stopped', TargetSoundTxt.tStopRefresh)
                    # the Routine "trial_separate" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 1 repeats of 'ThirdTD'
                
                
                # ------Prepare to start Routine "Pause1sec"-------
                continueRoutine = True
                routineTimer.add(1.000000)
                # update component parameters for each repeat
                # keep track of which components have finished
                Pause1secComponents = [PauseTxt2]
                for thisComponent in Pause1secComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                Pause1secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "Pause1sec"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = Pause1secClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=Pause1secClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *PauseTxt2* updates
                    if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        PauseTxt2.frameNStart = frameN  # exact frame index
                        PauseTxt2.tStart = t  # local t and not account for scr refresh
                        PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                        PauseTxt2.setAutoDraw(True)
                    if PauseTxt2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            PauseTxt2.tStop = t  # not accounting for scr refresh
                            PauseTxt2.frameNStop = frameN  # exact frame index
                            win.timeOnFlip(PauseTxt2, 'tStopRefresh')  # time at next scr refresh
                            PauseTxt2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in Pause1secComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "Pause1sec"-------
                for thisComponent in Pause1secComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thirdTDLoop.addData('PauseTxt2.started', PauseTxt2.tStartRefresh)
                thirdTDLoop.addData('PauseTxt2.stopped', PauseTxt2.tStopRefresh)
                
                # ------Prepare to start Routine "AddRespCountCode"-------
                continueRoutine = True
                # update component parameters for each repeat
                # keep track of which components have finished
                AddRespCountCodeComponents = []
                for thisComponent in AddRespCountCodeComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                AddRespCountCodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
                frameN = -1
                
                # -------Run Routine "AddRespCountCode"-------
                while continueRoutine:
                    # get current time
                    t = AddRespCountCodeClock.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=AddRespCountCodeClock)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in AddRespCountCodeComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "AddRespCountCode"-------
                for thisComponent in AddRespCountCodeComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                falsealarm = 0
                hitrate = 0
                if hit != 0:
                    falsealarm = 1-(hit/respcountP)
                    hitrate = hit/4
                
                TD.addData("RespCountP", respcountP)
                TD.addData("FalseAlarmRate", falsealarm)
                TD.addData("HitRate", hitrate)
                hit = 0
                respcountP = 0
                # the Routine "AddRespCountCode" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1 repeats of 'thirdTDLoop'
            
            thisExp.nextEntry()
            
        # completed 1 repeats of 'TD'
        
        
        # ------Prepare to start Routine "TakeBreak"-------
        continueRoutine = True
        # update component parameters for each repeat
        ContinueKey5.keys = []
        ContinueKey5.rt = []
        _ContinueKey5_allKeys = []
        # keep track of which components have finished
        TakeBreakComponents = [P2IntroTxt, ContinueTxt5, ContinueKey5]
        for thisComponent in TakeBreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TakeBreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TakeBreak"-------
        while continueRoutine:
            # get current time
            t = TakeBreakClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TakeBreakClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *P2IntroTxt* updates
            if P2IntroTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2IntroTxt.frameNStart = frameN  # exact frame index
                P2IntroTxt.tStart = t  # local t and not account for scr refresh
                P2IntroTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2IntroTxt, 'tStartRefresh')  # time at next scr refresh
                P2IntroTxt.setAutoDraw(True)
            
            # *ContinueTxt5* updates
            if ContinueTxt5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueTxt5.frameNStart = frameN  # exact frame index
                ContinueTxt5.tStart = t  # local t and not account for scr refresh
                ContinueTxt5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueTxt5, 'tStartRefresh')  # time at next scr refresh
                ContinueTxt5.setAutoDraw(True)
            
            # *ContinueKey5* updates
            waitOnFlip = False
            if ContinueKey5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey5.frameNStart = frameN  # exact frame index
                ContinueKey5.tStart = t  # local t and not account for scr refresh
                ContinueKey5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey5, 'tStartRefresh')  # time at next scr refresh
                ContinueKey5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ContinueKey5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ContinueKey5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ContinueKey5.status == STARTED and not waitOnFlip:
                theseKeys = ContinueKey5.getKeys(keyList=['space'], waitRelease=False)
                _ContinueKey5_allKeys.extend(theseKeys)
                if len(_ContinueKey5_allKeys):
                    ContinueKey5.keys = _ContinueKey5_allKeys[-1].name  # just the last key pressed
                    ContinueKey5.rt = _ContinueKey5_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TakeBreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TakeBreak"-------
        for thisComponent in TakeBreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('P2IntroTxt.started', P2IntroTxt.tStartRefresh)
        SLLoop.addData('P2IntroTxt.stopped', P2IntroTxt.tStopRefresh)
        SLLoop.addData('ContinueTxt5.started', ContinueTxt5.tStartRefresh)
        SLLoop.addData('ContinueTxt5.stopped', ContinueTxt5.tStopRefresh)
        # check responses
        if ContinueKey5.keys in ['', [], None]:  # No response was made
            ContinueKey5.keys = None
        SLLoop.addData('ContinueKey5.keys',ContinueKey5.keys)
        if ContinueKey5.keys != None:  # we had a response
            SLLoop.addData('ContinueKey5.rt', ContinueKey5.rt)
        SLLoop.addData('ContinueKey5.started', ContinueKey5.tStartRefresh)
        SLLoop.addData('ContinueKey5.stopped', ContinueKey5.tStopRefresh)
        # the Routine "TakeBreak" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "P2Welcome"-------
        continueRoutine = True
        # update component parameters for each repeat
        P2WelcomeContKey.keys = []
        P2WelcomeContKey.rt = []
        _P2WelcomeContKey_allKeys = []
        # keep track of which components have finished
        P2WelcomeComponents = [P2WelcomeTxt, P2WelcomeCont, P2WelcomeContKey]
        for thisComponent in P2WelcomeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        P2WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "P2Welcome"-------
        while continueRoutine:
            # get current time
            t = P2WelcomeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=P2WelcomeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *P2WelcomeTxt* updates
            if P2WelcomeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2WelcomeTxt.frameNStart = frameN  # exact frame index
                P2WelcomeTxt.tStart = t  # local t and not account for scr refresh
                P2WelcomeTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2WelcomeTxt, 'tStartRefresh')  # time at next scr refresh
                P2WelcomeTxt.setAutoDraw(True)
            
            # *P2WelcomeCont* updates
            if P2WelcomeCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2WelcomeCont.frameNStart = frameN  # exact frame index
                P2WelcomeCont.tStart = t  # local t and not account for scr refresh
                P2WelcomeCont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2WelcomeCont, 'tStartRefresh')  # time at next scr refresh
                P2WelcomeCont.setAutoDraw(True)
            
            # *P2WelcomeContKey* updates
            waitOnFlip = False
            if P2WelcomeContKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2WelcomeContKey.frameNStart = frameN  # exact frame index
                P2WelcomeContKey.tStart = t  # local t and not account for scr refresh
                P2WelcomeContKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2WelcomeContKey, 'tStartRefresh')  # time at next scr refresh
                P2WelcomeContKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(P2WelcomeContKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(P2WelcomeContKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if P2WelcomeContKey.status == STARTED and not waitOnFlip:
                theseKeys = P2WelcomeContKey.getKeys(keyList=['space'], waitRelease=False)
                _P2WelcomeContKey_allKeys.extend(theseKeys)
                if len(_P2WelcomeContKey_allKeys):
                    P2WelcomeContKey.keys = _P2WelcomeContKey_allKeys[-1].name  # just the last key pressed
                    P2WelcomeContKey.rt = _P2WelcomeContKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in P2WelcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "P2Welcome"-------
        for thisComponent in P2WelcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('P2WelcomeTxt.started', P2WelcomeTxt.tStartRefresh)
        SLLoop.addData('P2WelcomeTxt.stopped', P2WelcomeTxt.tStopRefresh)
        SLLoop.addData('P2WelcomeCont.started', P2WelcomeCont.tStartRefresh)
        SLLoop.addData('P2WelcomeCont.stopped', P2WelcomeCont.tStopRefresh)
        # check responses
        if P2WelcomeContKey.keys in ['', [], None]:  # No response was made
            P2WelcomeContKey.keys = None
        SLLoop.addData('P2WelcomeContKey.keys',P2WelcomeContKey.keys)
        if P2WelcomeContKey.keys != None:  # we had a response
            SLLoop.addData('P2WelcomeContKey.rt', P2WelcomeContKey.rt)
        SLLoop.addData('P2WelcomeContKey.started', P2WelcomeContKey.tStartRefresh)
        SLLoop.addData('P2WelcomeContKey.stopped', P2WelcomeContKey.tStopRefresh)
        # the Routine "P2Welcome" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "FamRatingIntro"-------
        continueRoutine = True
        # update component parameters for each repeat
        FamRateIntroKey.keys = []
        FamRateIntroKey.rt = []
        _FamRateIntroKey_allKeys = []
        # keep track of which components have finished
        FamRatingIntroComponents = [FamRateIntroTxt, FamIntroCont, FamRateIntroKey]
        for thisComponent in FamRatingIntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FamRatingIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FamRatingIntro"-------
        while continueRoutine:
            # get current time
            t = FamRatingIntroClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FamRatingIntroClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FamRateIntroTxt* updates
            if FamRateIntroTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FamRateIntroTxt.frameNStart = frameN  # exact frame index
                FamRateIntroTxt.tStart = t  # local t and not account for scr refresh
                FamRateIntroTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FamRateIntroTxt, 'tStartRefresh')  # time at next scr refresh
                FamRateIntroTxt.setAutoDraw(True)
            
            # *FamIntroCont* updates
            if FamIntroCont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FamIntroCont.frameNStart = frameN  # exact frame index
                FamIntroCont.tStart = t  # local t and not account for scr refresh
                FamIntroCont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FamIntroCont, 'tStartRefresh')  # time at next scr refresh
                FamIntroCont.setAutoDraw(True)
            
            # *FamRateIntroKey* updates
            waitOnFlip = False
            if FamRateIntroKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FamRateIntroKey.frameNStart = frameN  # exact frame index
                FamRateIntroKey.tStart = t  # local t and not account for scr refresh
                FamRateIntroKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FamRateIntroKey, 'tStartRefresh')  # time at next scr refresh
                FamRateIntroKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(FamRateIntroKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(FamRateIntroKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if FamRateIntroKey.status == STARTED and not waitOnFlip:
                theseKeys = FamRateIntroKey.getKeys(keyList=['space'], waitRelease=False)
                _FamRateIntroKey_allKeys.extend(theseKeys)
                if len(_FamRateIntroKey_allKeys):
                    FamRateIntroKey.keys = _FamRateIntroKey_allKeys[-1].name  # just the last key pressed
                    FamRateIntroKey.rt = _FamRateIntroKey_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FamRatingIntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FamRatingIntro"-------
        for thisComponent in FamRatingIntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('FamRateIntroTxt.started', FamRateIntroTxt.tStartRefresh)
        SLLoop.addData('FamRateIntroTxt.stopped', FamRateIntroTxt.tStopRefresh)
        SLLoop.addData('FamIntroCont.started', FamIntroCont.tStartRefresh)
        SLLoop.addData('FamIntroCont.stopped', FamIntroCont.tStopRefresh)
        # check responses
        if FamRateIntroKey.keys in ['', [], None]:  # No response was made
            FamRateIntroKey.keys = None
        SLLoop.addData('FamRateIntroKey.keys',FamRateIntroKey.keys)
        if FamRateIntroKey.keys != None:  # we had a response
            SLLoop.addData('FamRateIntroKey.rt', FamRateIntroKey.rt)
        SLLoop.addData('FamRateIntroKey.started', FamRateIntroKey.tStartRefresh)
        SLLoop.addData('FamRateIntroKey.stopped', FamRateIntroKey.tStopRefresh)
        # the Routine "FamRatingIntro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        FamRatingLoop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(cond + "_explicit.xlsx", selection='0:12'),
            seed=None, name='FamRatingLoop')
        thisExp.addLoop(FamRatingLoop)  # add the loop to the experiment
        thisFamRatingLoop = FamRatingLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisFamRatingLoop.rgb)
        if thisFamRatingLoop != None:
            for paramName in thisFamRatingLoop:
                exec('{} = thisFamRatingLoop[paramName]'.format(paramName))
        
        for thisFamRatingLoop in FamRatingLoop:
            currentLoop = FamRatingLoop
            # abbreviate parameter names if possible (e.g. rgb = thisFamRatingLoop.rgb)
            if thisFamRatingLoop != None:
                for paramName in thisFamRatingLoop:
                    exec('{} = thisFamRatingLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Pause1sec"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Pause1secComponents = [PauseTxt2]
            for thisComponent in Pause1secComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Pause1secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Pause1sec"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Pause1secClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Pause1secClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PauseTxt2* updates
                if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PauseTxt2.frameNStart = frameN  # exact frame index
                    PauseTxt2.tStart = t  # local t and not account for scr refresh
                    PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                    PauseTxt2.setAutoDraw(True)
                if PauseTxt2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        PauseTxt2.tStop = t  # not accounting for scr refresh
                        PauseTxt2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(PauseTxt2, 'tStopRefresh')  # time at next scr refresh
                        PauseTxt2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Pause1secComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Pause1sec"-------
            for thisComponent in Pause1secComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            FamRatingLoop.addData('PauseTxt2.started', PauseTxt2.tStartRefresh)
            FamRatingLoop.addData('PauseTxt2.stopped', PauseTxt2.tStopRefresh)
            
            # ------Prepare to start Routine "FamRating"-------
            continueRoutine = True
            # update component parameters for each repeat
            FamRatingResp.keys = []
            FamRatingResp.rt = []
            _FamRatingResp_allKeys = []
            Syllab1.setSound(Word11, secs=0.38, hamming=True)
            Syllab1.setVolume(1, log=False)
            Syllab2.setSound(Word12, secs=0.38, hamming=True)
            Syllab2.setVolume(1, log=False)
            Syllab3.setSound(Word13, secs=0.38, hamming=True)
            Syllab3.setVolume(1, log=False)
            # keep track of which components have finished
            FamRatingComponents = [FamRatePrompt, RatingScale, RatingScale2, FamRatingResp, Syllab1, Syllab2, Syllab3]
            for thisComponent in FamRatingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            FamRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "FamRating"-------
            while continueRoutine:
                # get current time
                t = FamRatingClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=FamRatingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *FamRatePrompt* updates
                if FamRatePrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FamRatePrompt.frameNStart = frameN  # exact frame index
                    FamRatePrompt.tStart = t  # local t and not account for scr refresh
                    FamRatePrompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FamRatePrompt, 'tStartRefresh')  # time at next scr refresh
                    FamRatePrompt.setAutoDraw(True)
                
                # *RatingScale* updates
                if RatingScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RatingScale.frameNStart = frameN  # exact frame index
                    RatingScale.tStart = t  # local t and not account for scr refresh
                    RatingScale.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RatingScale, 'tStartRefresh')  # time at next scr refresh
                    RatingScale.setAutoDraw(True)
                
                # *RatingScale2* updates
                if RatingScale2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    RatingScale2.frameNStart = frameN  # exact frame index
                    RatingScale2.tStart = t  # local t and not account for scr refresh
                    RatingScale2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RatingScale2, 'tStartRefresh')  # time at next scr refresh
                    RatingScale2.setAutoDraw(True)
                
                # *FamRatingResp* updates
                waitOnFlip = False
                if FamRatingResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FamRatingResp.frameNStart = frameN  # exact frame index
                    FamRatingResp.tStart = t  # local t and not account for scr refresh
                    FamRatingResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FamRatingResp, 'tStartRefresh')  # time at next scr refresh
                    FamRatingResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(FamRatingResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(FamRatingResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if FamRatingResp.status == STARTED and not waitOnFlip:
                    theseKeys = FamRatingResp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                    _FamRatingResp_allKeys.extend(theseKeys)
                    if len(_FamRatingResp_allKeys):
                        FamRatingResp.keys = _FamRatingResp_allKeys[-1].name  # just the last key pressed
                        FamRatingResp.rt = _FamRatingResp_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                # start/stop Syllab1
                if Syllab1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    Syllab1.frameNStart = frameN  # exact frame index
                    Syllab1.tStart = t  # local t and not account for scr refresh
                    Syllab1.tStartRefresh = tThisFlipGlobal  # on global time
                    Syllab1.play(when=win)  # sync with win flip
                if Syllab1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Syllab1.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Syllab1.tStop = t  # not accounting for scr refresh
                        Syllab1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Syllab1, 'tStopRefresh')  # time at next scr refresh
                        Syllab1.stop()
                # start/stop Syllab2
                if Syllab2.status == NOT_STARTED and tThisFlip >= 0.88-frameTolerance:
                    # keep track of start time/frame for later
                    Syllab2.frameNStart = frameN  # exact frame index
                    Syllab2.tStart = t  # local t and not account for scr refresh
                    Syllab2.tStartRefresh = tThisFlipGlobal  # on global time
                    Syllab2.play(when=win)  # sync with win flip
                if Syllab2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Syllab2.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Syllab2.tStop = t  # not accounting for scr refresh
                        Syllab2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Syllab2, 'tStopRefresh')  # time at next scr refresh
                        Syllab2.stop()
                # start/stop Syllab3
                if Syllab3.status == NOT_STARTED and tThisFlip >= 1.26-frameTolerance:
                    # keep track of start time/frame for later
                    Syllab3.frameNStart = frameN  # exact frame index
                    Syllab3.tStart = t  # local t and not account for scr refresh
                    Syllab3.tStartRefresh = tThisFlipGlobal  # on global time
                    Syllab3.play(when=win)  # sync with win flip
                if Syllab3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Syllab3.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Syllab3.tStop = t  # not accounting for scr refresh
                        Syllab3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Syllab3, 'tStopRefresh')  # time at next scr refresh
                        Syllab3.stop()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in FamRatingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "FamRating"-------
            for thisComponent in FamRatingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            FamRatingLoop.addData('FamRatePrompt.started', FamRatePrompt.tStartRefresh)
            FamRatingLoop.addData('FamRatePrompt.stopped', FamRatePrompt.tStopRefresh)
            FamRatingLoop.addData('RatingScale.started', RatingScale.tStartRefresh)
            FamRatingLoop.addData('RatingScale.stopped', RatingScale.tStopRefresh)
            FamRatingLoop.addData('RatingScale2.started', RatingScale2.tStartRefresh)
            FamRatingLoop.addData('RatingScale2.stopped', RatingScale2.tStopRefresh)
            # check responses
            if FamRatingResp.keys in ['', [], None]:  # No response was made
                FamRatingResp.keys = None
            FamRatingLoop.addData('FamRatingResp.keys',FamRatingResp.keys)
            if FamRatingResp.keys != None:  # we had a response
                FamRatingLoop.addData('FamRatingResp.rt', FamRatingResp.rt)
            FamRatingLoop.addData('FamRatingResp.started', FamRatingResp.tStartRefresh)
            FamRatingLoop.addData('FamRatingResp.stopped', FamRatingResp.tStopRefresh)
            Syllab1.stop()  # ensure sound has stopped at end of routine
            FamRatingLoop.addData('Syllab1.started', Syllab1.tStartRefresh)
            FamRatingLoop.addData('Syllab1.stopped', Syllab1.tStopRefresh)
            Syllab2.stop()  # ensure sound has stopped at end of routine
            FamRatingLoop.addData('Syllab2.started', Syllab2.tStartRefresh)
            FamRatingLoop.addData('Syllab2.stopped', Syllab2.tStopRefresh)
            Syllab3.stop()  # ensure sound has stopped at end of routine
            FamRatingLoop.addData('Syllab3.started', Syllab3.tStartRefresh)
            FamRatingLoop.addData('Syllab3.stopped', Syllab3.tStopRefresh)
            # the Routine "FamRating" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'FamRatingLoop'
        
        
        # ------Prepare to start Routine "AttentionCheck2"-------
        continueRoutine = True
        # update component parameters for each repeat
        AttentionKey2.keys = []
        AttentionKey2.rt = []
        _AttentionKey2_allKeys = []
        AttnCheck2Resp.setText('\n ')
        # keep track of which components have finished
        AttentionCheck2Components = [AttentionKey2, AttentionCheck2Txt, AttnCheck2Resp, AttnCheck2Cont]
        for thisComponent in AttentionCheck2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AttentionCheck2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AttentionCheck2"-------
        while continueRoutine:
            # get current time
            t = AttentionCheck2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AttentionCheck2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AttentionKey2* updates
            waitOnFlip = False
            if AttentionKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AttentionKey2.frameNStart = frameN  # exact frame index
                AttentionKey2.tStart = t  # local t and not account for scr refresh
                AttentionKey2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AttentionKey2, 'tStartRefresh')  # time at next scr refresh
                AttentionKey2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(AttentionKey2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(AttentionKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if AttentionKey2.status == STARTED and not waitOnFlip:
                theseKeys = AttentionKey2.getKeys(keyList=['1', '2', 'return'], waitRelease=False)
                _AttentionKey2_allKeys.extend(theseKeys)
                if len(_AttentionKey2_allKeys):
                    AttentionKey2.keys = _AttentionKey2_allKeys[-1].name  # just the last key pressed
                    AttentionKey2.rt = _AttentionKey2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *AttentionCheck2Txt* updates
            if AttentionCheck2Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AttentionCheck2Txt.frameNStart = frameN  # exact frame index
                AttentionCheck2Txt.tStart = t  # local t and not account for scr refresh
                AttentionCheck2Txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AttentionCheck2Txt, 'tStartRefresh')  # time at next scr refresh
                AttentionCheck2Txt.setAutoDraw(True)
            
            # *AttnCheck2Resp* updates
            if AttnCheck2Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AttnCheck2Resp.frameNStart = frameN  # exact frame index
                AttnCheck2Resp.tStart = t  # local t and not account for scr refresh
                AttnCheck2Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AttnCheck2Resp, 'tStartRefresh')  # time at next scr refresh
                AttnCheck2Resp.setAutoDraw(True)
            
            # *AttnCheck2Cont* updates
            if AttnCheck2Cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                AttnCheck2Cont.frameNStart = frameN  # exact frame index
                AttnCheck2Cont.tStart = t  # local t and not account for scr refresh
                AttnCheck2Cont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AttnCheck2Cont, 'tStartRefresh')  # time at next scr refresh
                AttnCheck2Cont.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AttentionCheck2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AttentionCheck2"-------
        for thisComponent in AttentionCheck2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if AttentionKey2.keys in ['', [], None]:  # No response was made
            AttentionKey2.keys = None
        SLLoop.addData('AttentionKey2.keys',AttentionKey2.keys)
        if AttentionKey2.keys != None:  # we had a response
            SLLoop.addData('AttentionKey2.rt', AttentionKey2.rt)
        SLLoop.addData('AttentionKey2.started', AttentionKey2.tStartRefresh)
        SLLoop.addData('AttentionKey2.stopped', AttentionKey2.tStopRefresh)
        SLLoop.addData('AttentionCheck2Txt.started', AttentionCheck2Txt.tStartRefresh)
        SLLoop.addData('AttentionCheck2Txt.stopped', AttentionCheck2Txt.tStopRefresh)
        SLLoop.addData('AttnCheck2Resp.text',AttnCheck2Resp.text)
        AttnCheck2Resp.reset()
        SLLoop.addData('AttnCheck2Resp.started', AttnCheck2Resp.tStartRefresh)
        SLLoop.addData('AttnCheck2Resp.stopped', AttnCheck2Resp.tStopRefresh)
        SLLoop.addData('AttnCheck2Cont.started', AttnCheck2Cont.tStartRefresh)
        SLLoop.addData('AttnCheck2Cont.stopped', AttnCheck2Cont.tStopRefresh)
        # the Routine "AttentionCheck2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Part2Intro2"-------
        continueRoutine = True
        # update component parameters for each repeat
        ContinueKey7.keys = []
        ContinueKey7.rt = []
        _ContinueKey7_allKeys = []
        # keep track of which components have finished
        Part2Intro2Components = [P2IntroTxt2, ContinueKey6, ContinueKey7]
        for thisComponent in Part2Intro2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Part2Intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Part2Intro2"-------
        while continueRoutine:
            # get current time
            t = Part2Intro2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Part2Intro2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *P2IntroTxt2* updates
            if P2IntroTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                P2IntroTxt2.frameNStart = frameN  # exact frame index
                P2IntroTxt2.tStart = t  # local t and not account for scr refresh
                P2IntroTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(P2IntroTxt2, 'tStartRefresh')  # time at next scr refresh
                P2IntroTxt2.setAutoDraw(True)
            
            # *ContinueKey6* updates
            if ContinueKey6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey6.frameNStart = frameN  # exact frame index
                ContinueKey6.tStart = t  # local t and not account for scr refresh
                ContinueKey6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey6, 'tStartRefresh')  # time at next scr refresh
                ContinueKey6.setAutoDraw(True)
            
            # *ContinueKey7* updates
            waitOnFlip = False
            if ContinueKey7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueKey7.frameNStart = frameN  # exact frame index
                ContinueKey7.tStart = t  # local t and not account for scr refresh
                ContinueKey7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueKey7, 'tStartRefresh')  # time at next scr refresh
                ContinueKey7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ContinueKey7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ContinueKey7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ContinueKey7.status == STARTED and not waitOnFlip:
                theseKeys = ContinueKey7.getKeys(keyList=['space'], waitRelease=False)
                _ContinueKey7_allKeys.extend(theseKeys)
                if len(_ContinueKey7_allKeys):
                    ContinueKey7.keys = _ContinueKey7_allKeys[-1].name  # just the last key pressed
                    ContinueKey7.rt = _ContinueKey7_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Part2Intro2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Part2Intro2"-------
        for thisComponent in Part2Intro2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('P2IntroTxt2.started', P2IntroTxt2.tStartRefresh)
        SLLoop.addData('P2IntroTxt2.stopped', P2IntroTxt2.tStopRefresh)
        SLLoop.addData('ContinueKey6.started', ContinueKey6.tStartRefresh)
        SLLoop.addData('ContinueKey6.stopped', ContinueKey6.tStopRefresh)
        # check responses
        if ContinueKey7.keys in ['', [], None]:  # No response was made
            ContinueKey7.keys = None
        SLLoop.addData('ContinueKey7.keys',ContinueKey7.keys)
        if ContinueKey7.keys != None:  # we had a response
            SLLoop.addData('ContinueKey7.rt', ContinueKey7.rt)
        SLLoop.addData('ContinueKey7.started', ContinueKey7.tStartRefresh)
        SLLoop.addData('ContinueKey7.stopped', ContinueKey7.tStopRefresh)
        # the Routine "Part2Intro2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        AFCTest = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(cond + "_explicit.xlsx", selection='12:28'),
            seed=None, name='AFCTest')
        thisExp.addLoop(AFCTest)  # add the loop to the experiment
        thisAFCTest = AFCTest.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAFCTest.rgb)
        if thisAFCTest != None:
            for paramName in thisAFCTest:
                exec('{} = thisAFCTest[paramName]'.format(paramName))
        
        for thisAFCTest in AFCTest:
            currentLoop = AFCTest
            # abbreviate parameter names if possible (e.g. rgb = thisAFCTest.rgb)
            if thisAFCTest != None:
                for paramName in thisAFCTest:
                    exec('{} = thisAFCTest[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "count"-------
            continueRoutine = True
            # update component parameters for each repeat
            AFCcount += 1
            QuestionNo = "Trial" + str(AFCcount) + " /16"
            # keep track of which components have finished
            countComponents = []
            for thisComponent in countComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            countClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "count"-------
            while continueRoutine:
                # get current time
                t = countClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=countClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in countComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "count"-------
            for thisComponent in countComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "count" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "AFCStart"-------
            continueRoutine = True
            routineTimer.add(1.500000)
            # update component parameters for each repeat
            QuestionNoTxt.setText(QuestionNo)
            # keep track of which components have finished
            AFCStartComponents = [QuestionNoTxt]
            for thisComponent in AFCStartComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AFCStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AFCStart"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AFCStartClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AFCStartClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *QuestionNoTxt* updates
                if QuestionNoTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    QuestionNoTxt.frameNStart = frameN  # exact frame index
                    QuestionNoTxt.tStart = t  # local t and not account for scr refresh
                    QuestionNoTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(QuestionNoTxt, 'tStartRefresh')  # time at next scr refresh
                    QuestionNoTxt.setAutoDraw(True)
                if QuestionNoTxt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > QuestionNoTxt.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        QuestionNoTxt.tStop = t  # not accounting for scr refresh
                        QuestionNoTxt.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(QuestionNoTxt, 'tStopRefresh')  # time at next scr refresh
                        QuestionNoTxt.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AFCStartComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AFCStart"-------
            for thisComponent in AFCStartComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            AFCTest.addData('QuestionNoTxt.started', QuestionNoTxt.tStartRefresh)
            AFCTest.addData('QuestionNoTxt.stopped', QuestionNoTxt.tStopRefresh)
            
            # ------Prepare to start Routine "AFCFirst"-------
            continueRoutine = True
            routineTimer.add(2.140000)
            # update component parameters for each repeat
            Word1No.setText('1')
            Word_1_1.setSound(Word11, secs=0.38, hamming=True)
            Word_1_1.setVolume(1, log=False)
            Word_1_2.setSound(Word12, secs=0.38, hamming=True)
            Word_1_2.setVolume(1, log=False)
            Word_1_3.setSound(Word13, secs=0.38, hamming=True)
            Word_1_3.setVolume(1, log=False)
            # keep track of which components have finished
            AFCFirstComponents = [Word1No, Word_1_1, Word_1_2, Word_1_3]
            for thisComponent in AFCFirstComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AFCFirstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AFCFirst"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AFCFirstClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AFCFirstClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Word1No* updates
                if Word1No.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Word1No.frameNStart = frameN  # exact frame index
                    Word1No.tStart = t  # local t and not account for scr refresh
                    Word1No.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Word1No, 'tStartRefresh')  # time at next scr refresh
                    Word1No.setAutoDraw(True)
                if Word1No.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word1No.tStartRefresh + 2.07-frameTolerance:
                        # keep track of stop time/frame for later
                        Word1No.tStop = t  # not accounting for scr refresh
                        Word1No.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word1No, 'tStopRefresh')  # time at next scr refresh
                        Word1No.setAutoDraw(False)
                # start/stop Word_1_1
                if Word_1_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    Word_1_1.frameNStart = frameN  # exact frame index
                    Word_1_1.tStart = t  # local t and not account for scr refresh
                    Word_1_1.tStartRefresh = tThisFlipGlobal  # on global time
                    Word_1_1.play(when=win)  # sync with win flip
                if Word_1_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word_1_1.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Word_1_1.tStop = t  # not accounting for scr refresh
                        Word_1_1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word_1_1, 'tStopRefresh')  # time at next scr refresh
                        Word_1_1.stop()
                # start/stop Word_1_2
                if Word_1_2.status == NOT_STARTED and tThisFlip >= 1.38-frameTolerance:
                    # keep track of start time/frame for later
                    Word_1_2.frameNStart = frameN  # exact frame index
                    Word_1_2.tStart = t  # local t and not account for scr refresh
                    Word_1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    Word_1_2.play(when=win)  # sync with win flip
                if Word_1_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word_1_2.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Word_1_2.tStop = t  # not accounting for scr refresh
                        Word_1_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word_1_2, 'tStopRefresh')  # time at next scr refresh
                        Word_1_2.stop()
                # start/stop Word_1_3
                if Word_1_3.status == NOT_STARTED and tThisFlip >= 1.76-frameTolerance:
                    # keep track of start time/frame for later
                    Word_1_3.frameNStart = frameN  # exact frame index
                    Word_1_3.tStart = t  # local t and not account for scr refresh
                    Word_1_3.tStartRefresh = tThisFlipGlobal  # on global time
                    Word_1_3.play(when=win)  # sync with win flip
                if Word_1_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word_1_3.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Word_1_3.tStop = t  # not accounting for scr refresh
                        Word_1_3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word_1_3, 'tStopRefresh')  # time at next scr refresh
                        Word_1_3.stop()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AFCFirstComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AFCFirst"-------
            for thisComponent in AFCFirstComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            AFCTest.addData('Word1No.started', Word1No.tStartRefresh)
            AFCTest.addData('Word1No.stopped', Word1No.tStopRefresh)
            Word_1_1.stop()  # ensure sound has stopped at end of routine
            AFCTest.addData('Word_1_1.started', Word_1_1.tStartRefresh)
            AFCTest.addData('Word_1_1.stopped', Word_1_1.tStopRefresh)
            Word_1_2.stop()  # ensure sound has stopped at end of routine
            AFCTest.addData('Word_1_2.started', Word_1_2.tStartRefresh)
            AFCTest.addData('Word_1_2.stopped', Word_1_2.tStopRefresh)
            Word_1_3.stop()  # ensure sound has stopped at end of routine
            AFCTest.addData('Word_1_3.started', Word_1_3.tStartRefresh)
            AFCTest.addData('Word_1_3.stopped', Word_1_3.tStopRefresh)
            
            # ------Prepare to start Routine "AFCSecond"-------
            continueRoutine = True
            routineTimer.add(2.140000)
            # update component parameters for each repeat
            Word_2_1.setSound(Word21, secs=0.38, hamming=True)
            Word_2_1.setVolume(1, log=False)
            Word_2_2.setSound(Word22, secs=0.38, hamming=True)
            Word_2_2.setVolume(1, log=False)
            Word_2_3.setSound(Word23, secs=0.38, hamming=True)
            Word_2_3.setVolume(1, log=False)
            # keep track of which components have finished
            AFCSecondComponents = [Word2No, Word_2_1, Word_2_2, Word_2_3]
            for thisComponent in AFCSecondComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AFCSecondClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AFCSecond"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AFCSecondClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AFCSecondClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Word2No* updates
                if Word2No.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Word2No.frameNStart = frameN  # exact frame index
                    Word2No.tStart = t  # local t and not account for scr refresh
                    Word2No.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Word2No, 'tStartRefresh')  # time at next scr refresh
                    Word2No.setAutoDraw(True)
                if Word2No.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word2No.tStartRefresh + 2.07-frameTolerance:
                        # keep track of stop time/frame for later
                        Word2No.tStop = t  # not accounting for scr refresh
                        Word2No.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word2No, 'tStopRefresh')  # time at next scr refresh
                        Word2No.setAutoDraw(False)
                # start/stop Word_2_1
                if Word_2_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    Word_2_1.frameNStart = frameN  # exact frame index
                    Word_2_1.tStart = t  # local t and not account for scr refresh
                    Word_2_1.tStartRefresh = tThisFlipGlobal  # on global time
                    Word_2_1.play(when=win)  # sync with win flip
                if Word_2_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word_2_1.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Word_2_1.tStop = t  # not accounting for scr refresh
                        Word_2_1.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word_2_1, 'tStopRefresh')  # time at next scr refresh
                        Word_2_1.stop()
                # start/stop Word_2_2
                if Word_2_2.status == NOT_STARTED and tThisFlip >= 1.38-frameTolerance:
                    # keep track of start time/frame for later
                    Word_2_2.frameNStart = frameN  # exact frame index
                    Word_2_2.tStart = t  # local t and not account for scr refresh
                    Word_2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    Word_2_2.play(when=win)  # sync with win flip
                if Word_2_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word_2_2.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Word_2_2.tStop = t  # not accounting for scr refresh
                        Word_2_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word_2_2, 'tStopRefresh')  # time at next scr refresh
                        Word_2_2.stop()
                # start/stop Word_2_3
                if Word_2_3.status == NOT_STARTED and tThisFlip >= 1.76-frameTolerance:
                    # keep track of start time/frame for later
                    Word_2_3.frameNStart = frameN  # exact frame index
                    Word_2_3.tStart = t  # local t and not account for scr refresh
                    Word_2_3.tStartRefresh = tThisFlipGlobal  # on global time
                    Word_2_3.play(when=win)  # sync with win flip
                if Word_2_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Word_2_3.tStartRefresh + 0.38-frameTolerance:
                        # keep track of stop time/frame for later
                        Word_2_3.tStop = t  # not accounting for scr refresh
                        Word_2_3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Word_2_3, 'tStopRefresh')  # time at next scr refresh
                        Word_2_3.stop()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AFCSecondComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AFCSecond"-------
            for thisComponent in AFCSecondComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            AFCTest.addData('Word2No.started', Word2No.tStartRefresh)
            AFCTest.addData('Word2No.stopped', Word2No.tStopRefresh)
            Word_2_1.stop()  # ensure sound has stopped at end of routine
            AFCTest.addData('Word_2_1.started', Word_2_1.tStartRefresh)
            AFCTest.addData('Word_2_1.stopped', Word_2_1.tStopRefresh)
            Word_2_2.stop()  # ensure sound has stopped at end of routine
            AFCTest.addData('Word_2_2.started', Word_2_2.tStartRefresh)
            AFCTest.addData('Word_2_2.stopped', Word_2_2.tStopRefresh)
            Word_2_3.stop()  # ensure sound has stopped at end of routine
            AFCTest.addData('Word_2_3.started', Word_2_3.tStartRefresh)
            AFCTest.addData('Word_2_3.stopped', Word_2_3.tStopRefresh)
            
            # ------Prepare to start Routine "AFCQuestion"-------
            continueRoutine = True
            # update component parameters for each repeat
            AFCResp.keys = []
            AFCResp.rt = []
            _AFCResp_allKeys = []
            # keep track of which components have finished
            AFCQuestionComponents = [QuestionTxt, AFCResp]
            for thisComponent in AFCQuestionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AFCQuestionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AFCQuestion"-------
            while continueRoutine:
                # get current time
                t = AFCQuestionClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AFCQuestionClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *QuestionTxt* updates
                if QuestionTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    QuestionTxt.frameNStart = frameN  # exact frame index
                    QuestionTxt.tStart = t  # local t and not account for scr refresh
                    QuestionTxt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(QuestionTxt, 'tStartRefresh')  # time at next scr refresh
                    QuestionTxt.setAutoDraw(True)
                
                # *AFCResp* updates
                waitOnFlip = False
                if AFCResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    AFCResp.frameNStart = frameN  # exact frame index
                    AFCResp.tStart = t  # local t and not account for scr refresh
                    AFCResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AFCResp, 'tStartRefresh')  # time at next scr refresh
                    AFCResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(AFCResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(AFCResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if AFCResp.status == STARTED and not waitOnFlip:
                    theseKeys = AFCResp.getKeys(keyList=['1', '2'], waitRelease=False)
                    _AFCResp_allKeys.extend(theseKeys)
                    if len(_AFCResp_allKeys):
                        AFCResp.keys = _AFCResp_allKeys[-1].name  # just the last key pressed
                        AFCResp.rt = _AFCResp_allKeys[-1].rt
                        # was this correct?
                        if (AFCResp.keys == str(AFCCorrect)) or (AFCResp.keys == AFCCorrect):
                            AFCResp.corr = 1
                        else:
                            AFCResp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AFCQuestionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AFCQuestion"-------
            for thisComponent in AFCQuestionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            AFCTest.addData('QuestionTxt.started', QuestionTxt.tStartRefresh)
            AFCTest.addData('QuestionTxt.stopped', QuestionTxt.tStopRefresh)
            # check responses
            if AFCResp.keys in ['', [], None]:  # No response was made
                AFCResp.keys = None
                # was no response the correct answer?!
                if str(AFCCorrect).lower() == 'none':
                   AFCResp.corr = 1;  # correct non-response
                else:
                   AFCResp.corr = 0;  # failed to respond (incorrectly)
            # store data for AFCTest (TrialHandler)
            AFCTest.addData('AFCResp.keys',AFCResp.keys)
            AFCTest.addData('AFCResp.corr', AFCResp.corr)
            if AFCResp.keys != None:  # we had a response
                AFCTest.addData('AFCResp.rt', AFCResp.rt)
            AFCTest.addData('AFCResp.started', AFCResp.tStartRefresh)
            AFCTest.addData('AFCResp.stopped', AFCResp.tStopRefresh)
            # the Routine "AFCQuestion" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'AFCTest'
        
        
        # ------Prepare to start Routine "HearingCheckIntro"-------
        continueRoutine = True
        # update component parameters for each repeat
        EndKey2.keys = []
        EndKey2.rt = []
        _EndKey2_allKeys = []
        # keep track of which components have finished
        HearingCheckIntroComponents = [HearingCheckTxt, EndKey2]
        for thisComponent in HearingCheckIntroComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        HearingCheckIntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "HearingCheckIntro"-------
        while continueRoutine:
            # get current time
            t = HearingCheckIntroClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=HearingCheckIntroClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *HearingCheckTxt* updates
            if HearingCheckTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                HearingCheckTxt.frameNStart = frameN  # exact frame index
                HearingCheckTxt.tStart = t  # local t and not account for scr refresh
                HearingCheckTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(HearingCheckTxt, 'tStartRefresh')  # time at next scr refresh
                HearingCheckTxt.setAutoDraw(True)
            
            # *EndKey2* updates
            waitOnFlip = False
            if EndKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EndKey2.frameNStart = frameN  # exact frame index
                EndKey2.tStart = t  # local t and not account for scr refresh
                EndKey2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EndKey2, 'tStartRefresh')  # time at next scr refresh
                EndKey2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EndKey2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EndKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EndKey2.status == STARTED and not waitOnFlip:
                theseKeys = EndKey2.getKeys(keyList=['space'], waitRelease=False)
                _EndKey2_allKeys.extend(theseKeys)
                if len(_EndKey2_allKeys):
                    EndKey2.keys = _EndKey2_allKeys[-1].name  # just the last key pressed
                    EndKey2.rt = _EndKey2_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in HearingCheckIntroComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "HearingCheckIntro"-------
        for thisComponent in HearingCheckIntroComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        SLLoop.addData('HearingCheckTxt.started', HearingCheckTxt.tStartRefresh)
        SLLoop.addData('HearingCheckTxt.stopped', HearingCheckTxt.tStopRefresh)
        # check responses
        if EndKey2.keys in ['', [], None]:  # No response was made
            EndKey2.keys = None
        SLLoop.addData('EndKey2.keys',EndKey2.keys)
        if EndKey2.keys != None:  # we had a response
            SLLoop.addData('EndKey2.rt', EndKey2.rt)
        SLLoop.addData('EndKey2.started', EndKey2.tStartRefresh)
        SLLoop.addData('EndKey2.stopped', EndKey2.tStopRefresh)
        # the Routine "HearingCheckIntro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        HearingcheckLoop = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('HearingCheckSounds.xlsx'),
            seed=None, name='HearingcheckLoop')
        thisExp.addLoop(HearingcheckLoop)  # add the loop to the experiment
        thisHearingcheckLoop = HearingcheckLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisHearingcheckLoop.rgb)
        if thisHearingcheckLoop != None:
            for paramName in thisHearingcheckLoop:
                exec('{} = thisHearingcheckLoop[paramName]'.format(paramName))
        
        for thisHearingcheckLoop in HearingcheckLoop:
            currentLoop = HearingcheckLoop
            # abbreviate parameter names if possible (e.g. rgb = thisHearingcheckLoop.rgb)
            if thisHearingcheckLoop != None:
                for paramName in thisHearingcheckLoop:
                    exec('{} = thisHearingcheckLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Pause1sec"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Pause1secComponents = [PauseTxt2]
            for thisComponent in Pause1secComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Pause1secClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Pause1sec"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Pause1secClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Pause1secClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PauseTxt2* updates
                if PauseTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PauseTxt2.frameNStart = frameN  # exact frame index
                    PauseTxt2.tStart = t  # local t and not account for scr refresh
                    PauseTxt2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PauseTxt2, 'tStartRefresh')  # time at next scr refresh
                    PauseTxt2.setAutoDraw(True)
                if PauseTxt2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PauseTxt2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        PauseTxt2.tStop = t  # not accounting for scr refresh
                        PauseTxt2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(PauseTxt2, 'tStopRefresh')  # time at next scr refresh
                        PauseTxt2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Pause1secComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Pause1sec"-------
            for thisComponent in Pause1secComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            HearingcheckLoop.addData('PauseTxt2.started', PauseTxt2.tStartRefresh)
            HearingcheckLoop.addData('PauseTxt2.stopped', PauseTxt2.tStopRefresh)
            
            # ------Prepare to start Routine "HearingCheck"-------
            continueRoutine = True
            # update component parameters for each repeat
            CheckWord.setSound(SoundFile, hamming=True)
            CheckWord.setVolume(1, log=False)
            WordOptions.setText("1. "+Word1 + "         2. " + Word2 + "         3. " + Word3)
            CheckRespKey.keys = []
            CheckRespKey.rt = []
            _CheckRespKey_allKeys = []
            # keep track of which components have finished
            HearingCheckComponents = [CheckWord, WordOptions, CheckQuestion, CheckRespKey]
            for thisComponent in HearingCheckComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            HearingCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "HearingCheck"-------
            while continueRoutine:
                # get current time
                t = HearingCheckClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=HearingCheckClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # start/stop CheckWord
                if CheckWord.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    CheckWord.frameNStart = frameN  # exact frame index
                    CheckWord.tStart = t  # local t and not account for scr refresh
                    CheckWord.tStartRefresh = tThisFlipGlobal  # on global time
                    CheckWord.play(when=win)  # sync with win flip
                
                # *WordOptions* updates
                if WordOptions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    WordOptions.frameNStart = frameN  # exact frame index
                    WordOptions.tStart = t  # local t and not account for scr refresh
                    WordOptions.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(WordOptions, 'tStartRefresh')  # time at next scr refresh
                    WordOptions.setAutoDraw(True)
                
                # *CheckQuestion* updates
                if CheckQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    CheckQuestion.frameNStart = frameN  # exact frame index
                    CheckQuestion.tStart = t  # local t and not account for scr refresh
                    CheckQuestion.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(CheckQuestion, 'tStartRefresh')  # time at next scr refresh
                    CheckQuestion.setAutoDraw(True)
                
                # *CheckRespKey* updates
                waitOnFlip = False
                if CheckRespKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    CheckRespKey.frameNStart = frameN  # exact frame index
                    CheckRespKey.tStart = t  # local t and not account for scr refresh
                    CheckRespKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(CheckRespKey, 'tStartRefresh')  # time at next scr refresh
                    CheckRespKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(CheckRespKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(CheckRespKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if CheckRespKey.status == STARTED and not waitOnFlip:
                    theseKeys = CheckRespKey.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                    _CheckRespKey_allKeys.extend(theseKeys)
                    if len(_CheckRespKey_allKeys):
                        CheckRespKey.keys = _CheckRespKey_allKeys[-1].name  # just the last key pressed
                        CheckRespKey.rt = _CheckRespKey_allKeys[-1].rt
                        # was this correct?
                        if (CheckRespKey.keys == str(Correct)) or (CheckRespKey.keys == Correct):
                            CheckRespKey.corr = 1
                        else:
                            CheckRespKey.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in HearingCheckComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "HearingCheck"-------
            for thisComponent in HearingCheckComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            CheckWord.stop()  # ensure sound has stopped at end of routine
            HearingcheckLoop.addData('CheckWord.started', CheckWord.tStartRefresh)
            HearingcheckLoop.addData('CheckWord.stopped', CheckWord.tStopRefresh)
            HearingcheckLoop.addData('WordOptions.started', WordOptions.tStartRefresh)
            HearingcheckLoop.addData('WordOptions.stopped', WordOptions.tStopRefresh)
            HearingcheckLoop.addData('CheckQuestion.started', CheckQuestion.tStartRefresh)
            HearingcheckLoop.addData('CheckQuestion.stopped', CheckQuestion.tStopRefresh)
            # check responses
            if CheckRespKey.keys in ['', [], None]:  # No response was made
                CheckRespKey.keys = None
                # was no response the correct answer?!
                if str(Correct).lower() == 'none':
                   CheckRespKey.corr = 1;  # correct non-response
                else:
                   CheckRespKey.corr = 0;  # failed to respond (incorrectly)
            # store data for HearingcheckLoop (TrialHandler)
            HearingcheckLoop.addData('CheckRespKey.keys',CheckRespKey.keys)
            HearingcheckLoop.addData('CheckRespKey.corr', CheckRespKey.corr)
            if CheckRespKey.keys != None:  # we had a response
                HearingcheckLoop.addData('CheckRespKey.rt', CheckRespKey.rt)
            HearingcheckLoop.addData('CheckRespKey.started', CheckRespKey.tStartRefresh)
            HearingcheckLoop.addData('CheckRespKey.stopped', CheckRespKey.tStopRefresh)
            # the Routine "HearingCheck" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'HearingcheckLoop'
        
        thisExp.nextEntry()
        
    # completed SLOrder repeats of 'SLLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'Randomization'


# ------Prepare to start Routine "P2End"-------
continueRoutine = True
# update component parameters for each repeat
EndAllKey.keys = []
EndAllKey.rt = []
_EndAllKey_allKeys = []
# keep track of which components have finished
P2EndComponents = [EndAllKey, FeedbackQ, EndMssg_Ver2]
for thisComponent in P2EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
P2EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "P2End"-------
while continueRoutine:
    # get current time
    t = P2EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=P2EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndAllKey* updates
    waitOnFlip = False
    if EndAllKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndAllKey.frameNStart = frameN  # exact frame index
        EndAllKey.tStart = t  # local t and not account for scr refresh
        EndAllKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndAllKey, 'tStartRefresh')  # time at next scr refresh
        EndAllKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EndAllKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EndAllKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EndAllKey.status == STARTED and not waitOnFlip:
        theseKeys = EndAllKey.getKeys(keyList=['return'], waitRelease=False)
        _EndAllKey_allKeys.extend(theseKeys)
        if len(_EndAllKey_allKeys):
            EndAllKey.keys = _EndAllKey_allKeys[-1].name  # just the last key pressed
            EndAllKey.rt = _EndAllKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *FeedbackQ* updates
    if FeedbackQ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FeedbackQ.frameNStart = frameN  # exact frame index
        FeedbackQ.tStart = t  # local t and not account for scr refresh
        FeedbackQ.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FeedbackQ, 'tStartRefresh')  # time at next scr refresh
        FeedbackQ.setAutoDraw(True)
    
    # *EndMssg_Ver2* updates
    if EndMssg_Ver2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndMssg_Ver2.frameNStart = frameN  # exact frame index
        EndMssg_Ver2.tStart = t  # local t and not account for scr refresh
        EndMssg_Ver2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndMssg_Ver2, 'tStartRefresh')  # time at next scr refresh
        EndMssg_Ver2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in P2EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "P2End"-------
for thisComponent in P2EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if EndAllKey.keys in ['', [], None]:  # No response was made
    EndAllKey.keys = None
thisExp.addData('EndAllKey.keys',EndAllKey.keys)
if EndAllKey.keys != None:  # we had a response
    thisExp.addData('EndAllKey.rt', EndAllKey.rt)
thisExp.addData('EndAllKey.started', EndAllKey.tStartRefresh)
thisExp.addData('EndAllKey.stopped', EndAllKey.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('FeedbackQ.started', FeedbackQ.tStartRefresh)
thisExp.addData('FeedbackQ.stopped', FeedbackQ.tStopRefresh)
thisExp.addData('EndMssg_Ver2.started', EndMssg_Ver2.tStartRefresh)
thisExp.addData('EndMssg_Ver2.stopped', EndMssg_Ver2.tStopRefresh)
# the Routine "P2End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

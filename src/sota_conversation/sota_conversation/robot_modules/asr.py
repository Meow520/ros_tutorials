import azure.cognitiveservices.speech as speechsdk
from queue import Queue

class ASR():
    def __init__(self, q:Queue, speech_api_key:str, service_region:str, lang:str):
        self.q = q
        self.speech_api_key = speech_api_key
        self.service_region = service_region
        self.lang = lang
        self.__done = False

    def start(self):
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_api_key, region=self.service_region)
        speech_config.speech_recognition_language=self.lang
        stream = speechsdk.audio.PushAudioInputStream()
        audio_config = speechsdk.audio.AudioConfig(stream=stream)

        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        self.speech_recognizer.recognizing.connect(self.__recognizing_cb)
        self.speech_recognizer.recognized.connect(self.__recognized_cb)
        self.speech_recognizer.session_started.connect(self.__session_started_cb)
        self.speech_recognizer.session_stopped.connect(self.__session_stopped_cb)
        self.speech_recognizer.canceled.connect(self.__canceled_cb)

    def __recognizing_cb(self, evt):
        obj = evt.result.text
        return obj

    def __recognized_cb(self, evt):
        obj = evt.result.text
        return obj

    def __session_started_cb(self, evt):
        print(f'Session started: {evt}')

    def __session_stopped_cb(self, evt):
        print(f'Session stopped: {evt}')
        global done
        self.__done = True

    def __canceled_cb(self, evt):
        print(f'CLOSING on {evt}')
        global done
        self.__done = True

    def __enter__(self):
        return self
    
    def __exit__(self):
        self.speech_recognizer.stop_continuous_recognition()

    
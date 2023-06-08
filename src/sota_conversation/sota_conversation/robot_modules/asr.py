"import packages"
import azure.cognitiveservices.speech as speechsdk


class ASR:
    "ASR definition"

    def __init__(self, q, speech_api_key: str, service_region: str, lang: str):
        self.__speech_api_key = speech_api_key
        self.__service_region = service_region
        self.__lang = lang
        self.__done = False
        self.__q = q

    def start(self):
        "starting sr"
        speech_config = speechsdk.SpeechConfig(
            subscription=self.__speech_api_key, region=self.__service_region
        )
        speech_config.speech_recognition_language = self.__lang
        stream = speechsdk.audio.PushAudioInputStream()
        audio_config = speechsdk.audio.AudioConfig(stream=stream)

        self.speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config, audio_config=audio_config
        )
        self.speech_recognizer.session_started.connect(self.__session_started_cb)
        self.speech_recognizer.session_stopped.connect(self.__session_stoped_cb)
        self.speech_recognizer.recognizing.connect(self.__recognizing_cb)
        self.speech_recognizer.recognized.connect(self.__recognized_cb)
        self.speech_recognizer.canceled.connect(self.__canceled_cb)

    def __enter__(self):
        return self

    def __exit__(self):
        self.speech_recognizer.stop_continuous_recognition()

    def __recognizing_cb(self, evt):
        obj = evt.result.text
        print(f"Recognizing: {obj}")

    def __recognized_cb(self, evt):
        obj = evt.result.text
        print(f"Recognized* {obj}")
        self.__q.put(obj)

    def __session_started_cb(self, evt):
        print(f"Session started: {evt}")

    def __session_stoped_cb(self, evt):
        print(f"Session stopped: {evt}")
        self.__done = True

    def __canceled_cb(self, evt):
        print(f"closing on {evt}")
        self.__done = True

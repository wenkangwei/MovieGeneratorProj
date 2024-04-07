#
#  Description: This file is the controller of the movie generator. It is responsible for the logic of 
#  editing resources like videos, images, and audio files, based on Langchain's API and moviepy library.
#  Date: 2021-09-26
#  Author: Wenkang wei
#  Reference: https://www.langchain.com.cn/modules/memory/getting_started
# 剪映： https://www.zhihu.com/question/573590101
# 
####################################################################################################
import langchain
import moviepy.editor as mppyth

class MovieOperation:
    def __init__(self) -> None:
        pass
    def gen_text_script(self, prompt:str):
        script = None
        raise NotImplementedError
        #return script
    
    def gen_subtitles(self, text:str):
        """
        generate subtitles/summary based on the text
        """
        subtitles = None
        raise NotImplementedError

    def gen_bgm(self, prompt:str):
        """
        generate background music based on the prompt
        """
        bgm = None
        raise NotImplementedError

    def gen_audio(self, prompt:str):
        """
        generate audio/huamn voice based on the prompt
        """
        audio = None
        raise NotImplementedError
        #return audio
    
    def gen_Img2Img(self, img, prompt:str):
        img = None
        raise NotImplementedError

    def gen_Img2Video(self, img, prompt:str):
        video = None
        raise NotImplementedError
    
    def update_video(self, video, prompt:str):
        video = None
        raise NotImplementedError
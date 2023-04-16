# KISAAN
## Documentation

Kisaan is designed to accuratley detect crop diseases within seconds. Kisaan detects problem in real time and shows accurate treatment solutions. Here is the best home farming app.

kisaan is a user friendly app that helps your plant to grow disease free. You can easily find the solution for your plant and get suggestions for healthy growth. kisaan helps you to make homemade fertilizers.

![main screen](https://user-images.githubusercontent.com/118742334/232313445-07133bb5-cbb1-4ce8-a471-ba16a5e8f816.png)


### Features
KISAAN trained in deep CNN with many layers to predict the diseases with high accuracy. It can also provide the solutions for insects and pathogens. Kisan was trained over 3 globally identified crop diseases(blackspots,cankerpowdery mildew). Kisan takes probabilities for the diseases to find the interlinked causes for the disease so that the solutions cures the plant quicker. Kisaan gives you notifications evrey day to water your plant.

![Disease Detection](https://bitrefine.group/images/1920x870/damaged_leaves_1920x870.jpg)

![cam](https://user-images.githubusercontent.com/118742334/232314381-f912d50a-be83-4c6b-8289-f7e36e9d076d.png)

![res](https://user-images.githubusercontent.com/118742334/232314385-12126f36-3f2b-494e-9e96-fbc733435f68.png)

### VRIKSH CHATBOT
Vriskh is an integrated chat bot. you can ask the solution for your problem to vriskh, he will help you with a solution(anthracnose,blackspots,blight,canker,downy mildew,fusarium wilt,mosaic,powdery mildew,rust,sooty mold,verticillium wilt).. He can guide you how to grow plants like rose ,jasmine,marigold etc and some domestic plants like brinjal,bittergourd,bottlegourd etc.


![vriksh](https://user-images.githubusercontent.com/118742334/232313429-47ae6858-afbd-4e1a-8abe-11b7d9007d5f.png)



### Version
1.0.0

![version](https://user-images.githubusercontent.com/118742334/232314237-e3b65522-205c-4c99-880a-b08e512a31f5.png)


#### Technologies used
* python
* kivy
* tenserflow/keras
* opencv


#### Graphs




![test1](https://user-images.githubusercontent.com/118742334/232312729-a5d1e473-4916-440d-9f52-bfeda635a9af.png)








To install the modules
```
pip install kivy
pip install tenserflow
pip install opencv-python
```
kivy [documentation](https://kivy.org/doc/stable/gettingstarted/intro.html "kivy")

tenserflow [documentation](https://www.tensorflow.org/api_docs/python/tf "tensorflow")

opencv [documentation](https://docs.opencv.org/4.x/d1/dfb/intro.html "opencv")
### APK

To build apk file I used buildozer. Buildozer currently works only in Linux and macOS (You can still use it on Windows via WSL), and can significantly simplify the apk build.
To install buildozer
```
pip install buildozer
```
This will install buildozer in your system. Afterwards, navigate to your project directory and run:
```
buildozer init
```
This creates a buildozer.spec file controlling your build configuration. You should edit it appropriately with your app name etc. You can set variables to control most or all of the parameters passed to python-for-android.
Finally, plug in your android device and run:
```
buildozer android debug deploy run
```
to build, push and automatically run the apk on your device.

buildozer [documnentation](https://kivy.org/doc/stable/guide/packaging-android.html "buildozer")

You can get buildozer at [https://github.com/kivy/buildozer](https://github.com/kivy/buildozer)


# Team

MUDUNURU SAI HARINI

SANNATH KOSUHIK SHARMAN

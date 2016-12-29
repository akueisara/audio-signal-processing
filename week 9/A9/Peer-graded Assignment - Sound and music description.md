### Task 1: Download sounds and descriptors from Freesound

###### Get sounds
1. SD.downloadSoundsFreesound(queryText='guitar', API_Key='', outputDir='testDownload/', topNResults=20, duration=(0,8), tag='guitar') </br>
2. SD.downloadSoundsFreesound(queryText='clarinet', API_Key= '', outputDir='testDownload/', topNResults=20, duration=(0,8), tag='single-note') </br>
3. SD.downloadSoundsFreesound(queryText='violin', API_Key='', outputDir='testDownload/', topNResults=20, duration=(0,8), tag='spiccato') </br>

###### Description
**guitar** 
query text: guitar </br>
tag: guitar </br>
duration: (0,8) </br>

**clarinet** 
query text: clarinet </br>
tag: single-note </br>
duration: (0,8) </br>

** violin** 
query text: cello </br>
tag: spiccato </br>
duration: (0,8) </br>

### Task 2: Select two descriptors for a good clustering of sounds in 2D

###### Descriptor pairs
5 -- lowlevel.spectral_contrast.mean.0 </br>
11 -- lowlevel.mfcc.mean.0 </br>
and </br>
9 -- lowlevel.spectral_contrast.mean.4 </br>
13 -- lowlevel.mfcc.mean.2 </br>

### Task 3: Cluster sounds of different instruments using kmeans in n-dimensions

###### Descriptors
5 - lowlevel.spectral_contrast.mean.0 </br>
8 - lowlevel.spectral_contrast.mean.3 </br>
11 - lowlevel.mfcc.mean.0 </br>

SA.clusterSounds('testDownload/', nCluster=3, descInput=[5,8,11]) </br>

###### Accuracy
95%

### Task 4: Classify a sound by using descriptors and a nearest neighbor classifier

###### Download test sound
SD.downloadSoundsFreesound(queryText='cello', API_Key='', outputDir='knn/', topNResults=5, duration=(0,5), tag='pizzicato') </br>
SD.downloadSoundsFreesound(queryText='bassoon', API_Key='', outputDir='knn/', topNResults=5,duration=(0,5), tag='multiphonic') </br>
SD.downloadSoundsFreesound(queryText='trumpet', API_Key='', outputDir='knn/', topNResults=5,duration=(0,5), tag='single-note') </br>
SD.downloadSoundsFreesound(queryText='guitar', API_Key='', outputDir='knn', topNResults=5,duration=(0,5), tag='acoustic') </br>

###### Parameters
descriptors:5,8,11 </br>
k:3 </br>

###### Classification
1. SA.classifySoundkNN('knn/cello/42256/42256_7037-lq.json', 'testDownload/', 3, descInput=[5,8,11]) </br>
   cello sound: https://www.freesound.org/people/Corsica_S/sounds/42256/  </br>
    => belongs to 'violin' </br>
2. SA.classifySoundkNN('knn/bassoon/90024/90024_976195-lq.json', 'testDownload/', 3, descInput=[5,8,11]) </br>
bassoon: https://www.freesound.org/people/tewell/sounds/90023/ </br>
=> belongs to 'guitar' </br>
3. SA.classifySoundkNN('knn/trumpet/357434/357434_6552981-lq.json', 'testDownload/', 3, descInput=[5,8,11]) </br>
trumpet: https://www.freesound.org/people/MTG/sounds/357434/ </br>
=> belongs to 'guitar' </br>
4. SA.classifySoundkNN('knn/guitar/58112/58112_4948-lq.json', 'testDownload/', 3, descInput=[5,8,11])
guitar: https://www.freesound.org/people/NoiseCollector/sounds/58112/
=> belongs to 'guitar' </br>
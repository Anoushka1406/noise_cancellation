# README #

### What is this repository for? ###

* Remove background noise from audio. 
* This algorithm identifies the backround noise profile by analyzing the "quiet" sections of the audio.
* It then creates a subtraction profile for the background noise and then adds that to the overall audio to remove the noise. 
* We are picking up noise clip data from lag+3000 to lag+15000 (you may change these according to your requirement).
* For better results you may also choose more "quiet" parts of the audio clip. 
* The key benefit of this method is that it created a differnet noiise reduction profiles for each audio.  Hence, it can work on many different noise environments and does not create any "metallic" soiund effects. 
* This wirks exactly like the human brain whichh takes the noise of the background and removes it form the consideration, by assuming it is is the background.


### How do I get set up? ###

* Install python3 along with  pandas, numpy, matplotlib and noisereduce

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact

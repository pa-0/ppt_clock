# ppt_clock
PPT countdown tool made on deepin system
This PPT countdown tool is a work-in-progress and quite buggy.

## What currently works:
1. Total time measurement;
2. How many minutes before the countdown will be played as a sound reminder;
3. How many seconds before the countdown starts;
4. Whether to play a prompt sound after the countdown ends;
5. After the countdown ends, whether to continue playing the PPT or close the PPT;
6. Whether to continue counting after the countdown ends;
	
## What doesn't:
1. When playing sound, the countdown pop-up window will freeze for a while. It seems to be a multi-threading issue in the code.
2. After the countdown ends, the only way to end the PowerPoint process is by killing it, as opposed to the script closing it as intended.
  
![image](https://user-images.githubusercontent.com/77780394/187358050-5fb322c4-075a-4efc-973d-07955f0c6fb4.png)  

![image](https://user-images.githubusercontent.com/77780394/187357774-3aa05863-2ad1-42c6-8fe3-50b6869d81f5.png)

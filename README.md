# happy_bot
## Introduction
This is a helper to help you decide what you can do in your free time, you can choose to watch movie, eat delicious food, or do some workout.

![](https://i.imgur.com/zLpD9En.png)


### movie
Introduce five movies 

![](https://i.imgur.com/9OPfFHW.png)




### eat
Choose what you want to eat now

![](https://i.imgur.com/nSGpzfL.png)




### workout

![](https://i.imgur.com/I88hJnf.png)

### show fsm

![](https://i.imgur.com/YcfFVJh.png)



## FSM Diagram

![](https://i.imgur.com/GG2u1cw.png)


## States
* ```user```
    * Input: "開始"
      * Reply: "*a button message* which allows to choose a kind activity & show fsm"
* ```menu```
    * Input: "看電影"
      * Reply: "a list of 5 introduced movies"
    * Input: "美食"
      * Reply: "*a button message* of 3 types of food"
    * Input: "健身"
      * Reply: "*a button message* to choose how long are you going to do your workout"
    * Input: "show fsm"
      * Reply: "show the fsm diagram"
* ```movie```
    
* ```eat```
    * Input: "正餐"
      * Reply: "*a button message* of 2 cities"
    * Input: "飲料"
      * Reply: "a list of 3 recommanded beverage shops around school"
    * Input: "點心"
      * Reply: "a list 3 recommanded dessert shops around school"
* ```workout```
    * Input: "15min"
      * Reply: "two videos about 15 minutes workout for beginners and seniors"
    * Input: "20min"
      * Reply: "two videos about 20 minutes workout for beginners and seniors"


* others...
  * Can always return to menu by entering 『開始』.
  * For states under ```eat``` can always enter 『美食』 to go back to ```eat``` menu.
  
   ![](https://i.imgur.com/VMKr2GL.png)



## Bonus
* Use web crawling to search movie & search city of popular food






# Team-253-Group-A-Backend

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8ba8b336227345f490088789142864bd)](https://app.codacy.com/gh/BuildForSDGCohort2/Team-253-Group-A-Backend?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDGCohort2/Team-253-Group-A-Backend&utm_campaign=Badge_Grade_Dashboard)

# Table of Contents

   * [Team-253-Group-A-Backend](#team-253-group-a-backend)
      * [About the team](#about-the-team)
      * [About our project "CleanOut"](#about-our-project-cleanout)
      * [User Guide](#user-guide)
         * [Step 1: Access the app &amp; Regsiter](#step-1-access-the-app--regsiter)
         * [Step 2: Fill in a trash report](#step-2-fill-in-a-trash-report)
         * [Step 3: Check reported spot(s)](#step-3-check-reported-spots)
         * [Step 4: Tour the app](#step-4-tour-the-app)
      * [Watch the video Walkthrough](#watch-the-video-walkthrough)
      * [Tutorials](#tutorials)
         * [Frontend Developement](#frontend-developement)
         * [Firebase Developement in Backend](#firebase-developement-in-backend)
         * [Try out our API](#try-out-our-api)
         * [Use the API](#use-the-api)
         * [Train the AI model](#train-the-ai-model)
         * [Learn how we collected the data](#learn-how-we-collected-the-data)
      * [License](#license)

## About the team

We are a team of 4 members: 

|[Front End Developer](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Frontend)|[Front End Developer](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Frontend)| [Back End Developer](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend)|[Technical Team Lead](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend)|
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img src="https://avatars1.githubusercontent.com/u/297917?s=460&v=4" width="100px" height="100px"> |  <img src="https://avatars2.githubusercontent.com/u/46009285?s=460&v=4" width="100px" height="100px"> | <img src="https://avatars2.githubusercontent.com/u/27445092?s=460&u=349cffccfccda38293e4aab20868a77b60079274&v=4" width="100px" height="100px"> | <img src="https://avatars1.githubusercontent.com/u/45902355?s=460&u=ffbc0cc593f575d67140e4197eec449a412a08c9v=4" width="100px" height="100px">|
|[Khalil Hammami](https://github.com/khammami)| [Ojoechem Chinonso](https://github.com/ChinonsoIg) | [Sara EL-ATEIF](https://github.com/elateifsara)| [Sofia Bourhim](https://github.com/SofiaBee-W) |

## About our project "CleanOut"

[CleanOut](https://awesome-jang-7f1fc2.netlify.app/) is an app built to help communities clean their neighborhood by letting users report trash by uploading (geotagged) image locations.  
Each report has a status (trash cleaned or not). Users can create an event to gather volunteers to help during the cleaning process.  
For COVID-19, AI will check if the uploaded images contain any COVID-19 trash like masks that needs precaution measures to clean. Or the user can choose to report to local authorities instead.

## User Guide

### Step 1: Access the app & Regsiter

Access the app by following this [link](https://awesome-jang-7f1fc2.netlify.app/).
You will be directed to the `Spots` section, that has all the reported trash spots.

To register or sign up please click on the `REGISTER` button on the upper right and either :  

- fill in the required information.        
  **Or**
- use on of the social media providers like your `Google` or `Facebook` account.  

If you have already created an account (Register), then please click on the `LOG IN` button on the upper right to log in and either:  

- fill in the required information.    
  **Or**  
- use on of the social media providers like your `Google` or `Facebook` account.    

### Step 2: Fill in a trash report

If you found trash in your neighborhood or on your walk then please report by clicking on the `New report` button on the left by the foot of the app or the `Report a spot of trash` button.  

- Allow access to the app to get your location.   
- Load the trash picture.   
- Wait until the AI analysis the picture (to check if there is any Covid-19 trash like mask, gloves, tissue or gel sanitizer).   
- Fill in the title, description, select the appropriate tags and the location of the trash site.   
- Wrap up by clicking on the `Create report` button.   

### Step 3: Check reported spot(s)

After you finished creating your report, you will directed to your spots; the ones you created. You can consult a spot by clicking on it.  

If you want to check all the reported spots, by you and other users, then go to the menu section and click on `Spots`.  

If you instead want to see only spots that have Covid-19 trash in them, then navigate to the `COVID-19` section in the menu.

Also, you can manage your account either with the edit or the delete by accessing `Your account` section.

### Step 4: Tour the app

You can also check out our :  

- `About` section to know more about the members.    
- `Terms of Service` & `Privacy Policy` sections.    

Or you can contact us by leaving us a message using the Contact us section.

## Watch the video Walkthrough

[![CleanOut Walkthrough](http://img.youtube.com/vi/_3QrxiEiD-s/0.jpg)](https://youtu.be/_3QrxiEiD-s "CleanOut Walkthrough")

## Tutorials

### Frontend Developement

Check out [the developement documention](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Frontend/blob/develop/documents/developpement.md) which contain all the steps needed to start developing on your local machine using ReactJs.

### Firebase Developement in Backend

Check out [the firebase developement tutorial](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/blob/develop/documents/FIREBASE-DEV-TUTORIAL.md): All tools you need to setup in order to test Firebase services locally without relying on the production environment of Firebase console..

### Try out the API 

Check out the simple JS [client example](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/tree/develop/ai_part/model_api/client), to know how to use the API.

### Use the API

Checkout the [model_api](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/tree/develop/ai_part/model_api) folder for the quickstart tutorial and the API reference.

### Train the AI model

Checkout the [modeling](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/tree/develop/ai_part/modeling) folder to train your own model using **Detetron2**.

### Learn how we collected the data

Checkout the [data_collection](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/tree/develop/ai_part/data_collection) folder to know how we collected the data needed to train the model.

## License

See the [LICENSE](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/blob/develop/LICENSE) file for license rights and limitations (MIT).

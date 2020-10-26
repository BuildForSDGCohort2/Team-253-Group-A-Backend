# Firebase developement tutorial

We're using firebase as part of our backend to accelerate the process of making prototype of our app (serverless):

- User authentification managed by Firebae auth.

- Data stored in database is managed by Firestore.

- Photos uploaded in our app is managed by Firebase storage.

- Scheldued tasks are managed by Firebase cloud functions.

To use Firebase in your proect your need to create a Firebase project using [Firebase console](https://console.firebase.google.com/).
and install [Firebase tools (CLI)](https://firebase.google.com/docs/cli)

## Requirement

A minimium of knowledge is required of the following frameworks and technologies:

- Node.js

- Firebase SDK

- Firestore

- Firebase Storage

- Firebase Cloud Functions

## 1. Install Firebase CLI (tools)

First you need to install Firebase tools using a method that matches your operating system by following [Firebase CLI documentation](https://firebase.google.com/docs/cli).

I'm using Ubuntu 20.04 for developement, so I'm running this command:

```shell
curl -sL firebase.tools | upgrade=true bash
```

## 2. Initialize Firebase project

After installing the CLI, you must authenticate.

1. Log into Firebase using you Google account:

```shell
firebase login
```

2. Link your Firebase project and initialize it inside backend folder:

```shell
firebase init
```

The `firebase init` command steps you through setting up your project directory and some Firebase products.

At the end of initialization, Firebase automatically creates the following two files at the root of your local app directory:

- A [firebase.json](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/blob/develop/firebase.json) configuration file that lists your project configuration.

- A [.firebaserc](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/blob/develop/.firebaserc) file that stores your project aliases.

## 3. Setup Firebase Local Emulator

For your developement & test, It would be better to run it locally rather using production envirement to test your work.

Firebase provide a local emulator for almost all their services to test aigaint them locally: [Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite)

Emulator suite is part Firebase CLI, so all you need now is to run this command:

```shell
firebase init emulators
```

For more information about ho to install and configure emulators, check "[Install, configure and integrate](https://firebase.google.com/docs/emulator-suite/install_and_configure)"

After setting up the emulators, run this command to start them:

```shell
firebase emulators:start
```

## 4. Deployment

The Firebase CLI manages deployment of code and assets to your Firebase project, including:

- [New, updated, or existing Cloud Functions for Firebase](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/tree/develop/functions)

- [Rules for Cloud Storage for Firebase](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/blob/develop/storage.rules)

- [Rules for Cloud Firestore](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/blob/develop/firestore.rules)

- [Indexes for Cloud Firestore](https://github.com/BuildForSDGCohort2/Team-253-Group-A-Backend/blob/develop/firestore.indexes.json)

Command list we need for our project are the following:

- Cloud Storage for Firebase rules

```shell
firebase deploy --only storage
```

- Cloud Firestore rules and indexes

```shell
firebase deploy --only firestore
```

- Cloud Firestore rules

```shell
firebase deploy --only firestore:rules
```

- Cloud Firestore indexes

```shell
firebase deploy --only firestore:indexes
```

- Cloud Functions for Firebase

```shell
firebase deploy --only functions
```

You may combine all these commands into one command:

```shell
firebase deploy --only functions,firestore,storage
```

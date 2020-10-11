const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

exports.createUserProfile = functions.auth.user().onCreate((user) => {
  const db = admin.firestore();
  const batch = db.batch();

  const createSettingsRef = db.collection("users").doc(user.uid);
  batch.set(createSettingsRef, {
    uid: user.uid,
    displayName: user.displayName,
    photoURL: user.photoURL,
    createdAt: user.metadata.creationTime,
    email: user.email,
    phoneNumber: user.phoneNumber,
    isVerified: user.emailVerified,
    disabled: user.disabled,
    profile: db.collection("profiles").doc(user.uid),
  });

  const createProfileRef = db.collection("profiles").doc(user.uid);
  batch.set(createProfileRef, {
    uid: user.uid,
    displayName: user.displayName,
    photoURL: user.photoURL,
    createdAt: user.metadata.creationTime,
    isVerified: user.emailVerified,
    disabled: user.disabled,
  });

  return batch.commit();
});

exports.updateUserProfile = functions.firestore
  .document("users/{userId}")
  .onUpdate((change, context) => {
    const db = admin.firestore();
    const newValue = change.after.data();

    db.collection("profiles")
      .doc(context.params.userId)
      .update({ displayName: newValue.displayName });
  });

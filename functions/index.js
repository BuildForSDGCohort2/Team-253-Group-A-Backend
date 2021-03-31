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

    return db
      .collection("profiles")
      .doc(context.params.userId)
      .update({ displayName: newValue.displayName });
  });

exports.clearUserData = functions.auth.user().onDelete(async (user) => {
  const { uid } = user;
  const firestore = admin.firestore();

  const pathsToDelete = ["/users/" + uid, "/profiles/" + uid];

  const spotsRef = firestore.collection("spots");
  const snapshot = await spotsRef.where("uid", "==", uid).get();
  if (!snapshot.empty) {
    snapshot.forEach((doc) => {
      pathsToDelete.push("/spots/" + doc.id);
    });
  }

  const promises = [];
  if (pathsToDelete) {
    promises.push(clearFirestoreData(pathsToDelete));
  }

  await Promise.all(promises);
  console.log("user data has been cleared uid: " + uid);
});

const clearFirestoreData = async (paths) => {
  const promises = paths.map(async (path) => {
    try {
      const firestore = admin.firestore();
      // Wrapping in transaction to allow for automatic retries (#48)
      await firestore.runTransaction((transaction) => {
        transaction.delete(firestore.doc(path));
        return Promise.resolve();
      });
      console.log("doc path deleted: " + path);
    } catch (err) {
      console.log(path + "-" + err);
    }
  });

  await Promise.all(promises);
};

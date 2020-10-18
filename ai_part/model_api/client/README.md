# Client Example

## Run

Run the following in your terminal:

```sh
npm install
npm install -g browserify
npm install -g watchify
npm i konva
npm i xhr-request
watchify index.js -o bundle.js
```

After this click on `index.html` to visualize the results.

**NB:**
I run the docker in parallel for now until I deploy the API.  
Remember to type `docker run -p 8484:5000 -it your_user_name/detectron2:cleanout_v0 bin/bas` to do so.  
Also, notice that some websites hosting images have a bit strict CORS policies so not all images will work fine. But you can check out the response using the inspectore `console` section.  

After you deploy in Azure, change the local address to your new API address.

## References

[Reference on which this work is based upon.](https://towardsdatascience.com/detectron2-the-basic-end-to-end-tutorial-5ac90e2f90e3)

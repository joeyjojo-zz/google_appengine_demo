var AnyBlog;

AnyBlog = (function() {
    var handleGetMorePostsClick, getNextPostsData, setCurrentIndex, generateBlogPostHTML, addErrorMessage, addLoading,
        removeLoading;
    var currIndex = 0;

    /*
     * Add an error message to the page
     */
    addErrorMessage = function(msg) {

    };

    /*
     * Add a loading message to the page
     */
    addLoading = function(){
        
    };

    /*
     * Remove the loading page from the screen
     */
    removeLoading = function(){
        
    };


    // TODO: These probably belong in a separate file as they are only used on the index page
    /*
     * getNextPostsData
     * Retreives the data from the server in json format for the
     * next num posts
     */
    getNextPostsData = function(num) {
        return $.getJSON('/anyblog/next/'+num+'/'+currIndex);
    };

    /*
     * handleGetMorePostsClick
     * Handles the click event from the "Get next 5 posts..." link
     * Grabs the data from the server and inserts it into the dom
     */
    handleGetMorePostsClick = function(num, elem) {
        // add loading symbol
        addLoading();
        // get the data
        $.when(getNextPostsData(num))
            .then(function(data) {
                // parse the data
                var l = [];
                for (var i=0, len=data.length; i<len; i++){
                    l.push(generateBlogPostHTML(data[i]));
                }
                // insert the html
                elem.append(l.join(""));
                // clean up
                setCurrentIndex(currIndex+data.length);
                removeLoading();
            })
            .fail(function() {
                // add error message
                addErrorMessage("Failed to load blog posts.");
                // clean up
                removeLoading();
            });
    };

    /*
     * generateBlogPostHTML
     * generates html for the blog post item based on blogpostdata
     */
    generateBlogPostHTML = function(blogpostdata){
        // this is a bit foolish but I didn't know whether it was
        // better to let django do all the template work or whether
        // to include a javascript templating library as a general rule for issues like this
        // one keeps data sent from the server smaller,
        // other keeps all templates generated on the server and doesn't lead to a mix of templating styles
        var textArr = []
        var fields = blogpostdata["fields"];
        textArr.push("<h1>");
        textArr.push(fields["title"]);
        textArr.push("</h1>");
        textArr.push("<p>");
        textArr.push(fields["content"]);
        textArr.push("</p>");
        textArr.push("<ul>");
        textArr.push("<li>");
        textArr.push("<a href='/anyblog/");
        textArr.push(blogpostdata["pk"]);
        textArr.push("'>View</a></li>");
        textArr.push("<li>");
        textArr.push("<a href='/admin/anyblog/blogpost/");
        textArr.push(blogpostdata["pk"]);
        textArr.push("'>Edit</a></li>");
        textArr.push("<li>");
        textArr.push("<a href='/admin/anyblog/blogpost/");
        textArr.push(blogpostdata["pk"]);
        textArr.push("/delete'>Delete</a></li>");
        textArr.push("</ul>");
        textArr.push("<p>");
        textArr.push(fields["author"]);
        textArr.push("</p>");
        textArr.push("<p>");
        textArr.push(fields["timestampcreated"]);
        textArr.push("</p>");
        if (fields["timestampcreated"] !== fields["timestampmodified"]){
            textArr.push("<p>Last edited on ");
            textArr.push(fields["timestampmodified"]);
            textArr.push("</p>");
        }
        return textArr.join("");
    };

    /*
     * setCurrentIndex
     * set the current index of the viewable blog post
     */
    setCurrentIndex = function(val){
        currIndex = val;
    };

    return {handleGetMorePostsClick:handleGetMorePostsClick,
            setCurrentIndex:setCurrentIndex};
})();
var AnyBlog;

AnyBlog = (function() {
    var handleGetMorePostsClick, getNextPostsData, setCurrentIndex, generateBlogPostHTML, addErrorMessage, addLoading,
        removeLoading;
    var currIndex = 0;

    /*
     * Add an error message to the page
     */
    addErrorMessage = function(msg) {
        $("#error").append("<div class='error-message'>" + msg + "</div>");
    };

    /*
     * Add a loading message to the page
     */
    addLoading = function(elem){
        if (elem === undefined){
            elem = $("#info");
        };
        elem.append("<div id='loading_message' class='loading-message'>Loading...</div>");
    };

    /*
     * Remove the loading page from the screen
     */
    removeLoading = function(){
        $("#loading_message").remove();
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
        addLoading(elem);
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
                $(".blog-post-widget-content a").button();
                setCurrentIndex(currIndex+data.length);
                removeLoading(elem);
            })
            .fail(function() {
                // add error message
                addErrorMessage("Failed to load blog posts.");
                // clean up
                removeLoading(elem);
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
        textArr.push("<div class='ui-widget blog-post-widget'>");
        textArr.push("<div class='ui-widget-header'>");
        textArr.push("<h1>");
        textArr.push(fields["title"]);
        textArr.push("</h1>");
        textArr.push("</div>");
        textArr.push("<div class='ui-widget-content blog-post-widget-content'>");
        textArr.push("<p>");
        textArr.push(fields["content"]);
        textArr.push("</p>");
        textArr.push("<a href='/anyblog/");
        textArr.push(blogpostdata["pk"]);
        textArr.push("'>View</a>");
        textArr.push("<a href='/admin/anyblog/blogpost/");
        textArr.push(blogpostdata["pk"]);
        textArr.push("'>Edit</a>");
        textArr.push("<a href='/admin/anyblog/blogpost/");
        textArr.push(blogpostdata["pk"]);
        textArr.push("/delete'>Delete</a>");
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
        textArr.push("</div>");
        textArr.push("</div>");
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
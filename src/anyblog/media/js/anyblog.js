var AnyBlog;

AnyBlog = (function() {
    var handleGetMorePostsClick, getNextPostsData;
    var currIndex = 0;

    /*
     * getNext5PostsData
     * Retreives the data from the server in json format for the
     * next 5 posts
     */
    getNextPostsData = function(num) {
        return $.getJSON('/anyblog/next/'+num+'/'+currIndex);
    };

    /*
     * handleGetNext5PostsClick
     * Handles the click event from the "Get next 5 posts..." link
     * Grabs the data from the server and inserts it into the dom
     */
    handleGetMorePostsClick = function(num) {
        $.when(getNextPostsData(num))
            .then(function() {
                alert("data retrieved!");
            })
            .fail(function() {
                alert("data failed!");
            });
    };

    return {handleGetMorePostsClick:handleGetMorePostsClick,
            currIndex:currIndex};
})();
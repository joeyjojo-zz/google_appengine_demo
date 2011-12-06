var AnyBlog;

AnyBlog = (function() {
    var handleGetNext5PostsClick, getNext5PostsData;

    /*
     * handleGetNext5PostsClick
     * Handles the click event from the "Get next 5 posts..." link
     * Grabs the data from the server and inserts it into the dom
     */
    handleGetNext5PostsClick = function() {
        $.when(getNext5PostsData())
            .then(function() {

            })
            .fail(function() {

            });
    };

    /*
     * getNext5PostsData
     * Retreives the data from the server in json format for the
     * next 5 posts
     */
    getNext5PostsData = function() {
        return $.getJSON('/anyblog/');
    };

    return {handleGetNext5PostsClick:handleGetNext5PostsClick};
})();
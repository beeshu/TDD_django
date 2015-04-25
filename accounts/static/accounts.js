/**
 * Created by xzw on 2015/4/25.
 */

var initialize = function (navigator, user, token, urls) {

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            $.post(
                urls.login,
                {assertion: assertion, csrfmiddlewaretoken: token}
            );
        },
        onlogout: function() {

        }
    });

    $('#id_login').on('click', function () {
        navigator.id.request();
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};


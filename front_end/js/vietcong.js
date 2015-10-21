$.extend({
    vietcong: {
        updateEmails: function() {
            $('a.email').nospam({
                filterLevel: 'low',
                replaceText: true
            });
        }
    }
});

$(document).ready(function() {
    $(document).foundation({
        topbar: {
            custom_back_text: false,
        },
    });

    $.vietcong.updateEmails();
});

$(document).on('click', 'button.close', function() {
    $(this).parent().fadeTo('slow', 0).hide('slow');
});

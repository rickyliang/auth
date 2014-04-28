$(document).ready(function() {
    
    var password_help_title = 'Tips for Creating a Password';
    var password_help_content = 'Make sure your password is at least 8 characters long and includes UPPERCASE and lowercase letters and numbers.<br>\
    Consider using long, catchy-but-unique (thus relatively easy-to-remember) phrases since they are known to be effective passwords.<br><br>\
    For example, consider the passwords "thedogisnamedToady8" and "nq7TS%h". They both would take an estimated 100+ years for a hacker to crack. Choosing one over the other depends entirely on personal preference, but this is something to keep in mind as a possibility when creating passwords. It does not necessarily need to be difficult to remember.';
    $('#password_help').popover({container: 'body', trigger: 'hover focus', title: password_help_title, content: password_help_content, html: true});
    
    
    
    $('#password').keyup(function() {
        var password_value = $(this).val();
        var result = zxcvbn(password_value);
        var result_bar = $('#password_bar').children();
        
        if (result_bar.hasClass('bg-danger')) {
            result_bar.removeClass('bg-danger');
        } else if (result_bar.hasClass('bg-warning')) {
            result_bar.removeClass('bg-warning');
        } else if (result_bar.hasClass('bg-success')) {
            result_bar.removeClass('bg-success');
        }
        
        if (password_value.length > 0) {
            if (result.score <= 1) {
                result_bar.eq(0).addClass('bg-danger');
            } else if (result.score <= 2) {
                result_bar.eq(0).addClass('bg-danger');
                result_bar.eq(1).addClass('bg-danger');
            } else if (result.score <= 3) {
                result_bar.eq(0).addClass('bg-warning');
                result_bar.eq(1).addClass('bg-warning');
                result_bar.eq(2).addClass('bg-warning');
            } else {
                result_bar.eq(0).addClass('bg-success');
                result_bar.eq(1).addClass('bg-success');
                result_bar.eq(2).addClass('bg-success');
                result_bar.eq(3).addClass('bg-success');
            }
        }
    });
    
    /** Old password strength display using glyphicons.
    $('#password_result').tooltip({container: 'body', trigger: 'hover focus'});
    $('#password').keyup(function() {
        var password_value = $(this).val();
        var result = zxcvbn(password_value);
        var result_span = $('#password_result');
        
        // Reset #password_result to have no glyphicons
        if (result_span.hasClass('glyphicon-remove')) {
            result_span.removeClass('glyphicon-remove');
        } else if (result_span.hasClass('glyphicon-warning-sign')) {
            result_span.removeClass('glyphicon-warning-sign');
        } else if (result_span.hasClass('glyphicon-ok')) {
            result_span.removeClass('glyphicon-ok');
        }
        
        // Add appropriate glyphicon to #password_result if password_value.length != 0
        if (password_value.length > 0) {
            if (result.score < 2) {
                result_span.addClass('glyphicon-remove');
            } else if (result.score < 3) {
                result_span.addClass('glyphicon-warning-sign');
            } else {
                result_span.addClass('glyphicon-ok');
            }
        } else {
            result_span.attr('hidden', 'true');
        }
        
        // http://stackoverflow.com/questions/9501921/change-twitter-bootstrap-tooltip-content-on-click
        var password_result_content = 'Score: ' + result.score + '/4';
        result_span.attr('title', password_result_content);
        result_span.tooltip('fixTitle');
    });
    */
});
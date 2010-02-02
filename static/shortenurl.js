var shorten = {
    init : function () {
        shorten.form = document.getElementById('url_input_form');
        YAHOO.util.Event.addListener(shorten.form, 'submit', shorten.submitted);
    },
    
    submitted : function (e) {
        YAHOO.util.Event.preventDefault(e);
        YAHOO.util.Connect.setForm(shorten.form);
        YAHOO.util.Connect.asyncRequest('POST', '/', shorten.process_json);
    },
    
    process_json : {
        success: function (o) {
            var response = JSON.parse(o.responseText);
            if (response.success) {
                shorten.output = document.getElementById('url_input_div');
                shorten.success_result(shorten.output, response.url, response.short);
            }
            else if (response.error) {
                shorten.output = document.getElementById('url_input_div');
                shorten.error_result(shorten.output, response.msg);
            }
        },  
        
        failure : function (o) {
        }
    },
    
    success_result : function (element, url, shorturl) {
        var output_info = shorten.reset_output_div(),
        short_label = document.createElement('label'),
        short_value = document.createElement('input'),
        original = document.createElement('p');

        shorten.form.reset();
        short_label.htmlFor = "out";
        short_label.innerHTML = "Short URL:";
        
        short_value.name = "out";
        short_value.className = "url_text";
        short_value.value = shorturl;
        short_value.type = "text";
        
        original.innerHTML = "Original URL: " + url;
        
        output_info.appendChild(short_label);
        output_info.appendChild(short_value);
        output_info.appendChild(original);
        shorten.output.appendChild(output_info);
    },
    
    error_result : function (element, msg) {
        var output_info = shorten.reset_output_div(),
        message = document.createElement('p');
        message.className = "error";
        message.innerHTML = msg;
        output_info.appendChild(message);
        shorten.output.appendChild(output_info);
    },
    
    reset_output_div : function() {
        var output_info = document.getElementById('short_url_info');
        if (output_info !== null) {
            shorten.output.removeChild(output_info);
        }
        output_info = document.createElement('div');
        output_info.id = 'short_url_info';
        return output_info;
    }
};

YAHOO.util.Event.addListener(window, 'load', shorten.init);
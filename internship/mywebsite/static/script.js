// console.log(window.location)



$("#website-url").on("change", function(){
    let select_val = $("#website-url").val();
    // alert("url type: "+ select_val)
    switch (select_val) {
        case "interesting_urls":
            $("#fetchDataForm").attr("action", "/fetchInterestingUrl");
            break;
        case "non_interesting_urls":
            $("#fetchDataForm").attr("action", "/fetchNonInterestingUrl");
            break;
        default:
                $("#fetchDataForm").attr("action", "/fetchInterestingUrl");
            break;
    }
    
});



var url_string = window.location;
var url = new URL(url_string);
var website = url.searchParams.get("website");
let urlType = url.searchParams.get("urls");
// console.log(website, urlType);
console.log(website)
if(website != null){
    document.getElementById('website-select').value = website;
}
if(urlType != null){
    document.getElementById('website-url').value = urlType;
}

$("#url-type-show").text(website);
$("#website-show").text(urlType)

let loginForm = '<form method="POST" id="signup-form" class="signup-form"> <h2 class="form-title">Login</h2> <div class="form-group"> <input type="email" class="form-input" name="email" id="email" placeholder="Your Email" autocomplete="none"/> </div> <div class="form-group"> <input type="text" class="form-input" name="password" id="password" placeholder="Password" autocomplete="none"/> <span toggle="#password" class="zmdi zmdi-eye field-icon toggle-password"></span> </div> <div class="form-group"> <input type="password" class="form-input" name="re_password" id="re_password" placeholder="Repeat your password" autocomplete="none"/> </div> <div class="form-group"> <input type="checkbox" name="agree-term" id="agree-term" class="agree-term" /> <label for="agree-term" class="label-agree-term"><span><span></span></span>I agree all statements in <a href="#" class="term-service">Terms of service</a></label> </div> <div class="form-group"> <input type="submit" name="submit" id="submit" class="form-submit" value="Sign up"/> </div> </form>';



$(".scraping-processing").hide();
$(".scraping-btn").click(function() {
    $('.scraping-btn').attr("disabled", true);
    website = $(this).attr('id');
    switch (website) {
        case 'eventshigh.com':
            $("#eventshigh_com_processing").show();
            break;
        case 'insider.in':
            $("#insider_in_processing").show();
            break;
        case 'naadyogacouncil.com':
            $('#naadyogacouncil_com_processing').show();
        default:
            break;
    }
    console.log(website);
    $.ajax({
        url: "/scraping_admin/",
        type: 'GET',
        data: {'website': website},
        success: function(data){
            alert("Scraping Successful!")
            console.log("Success");

            location.reload(); 
        }
    })
})
$(function(){
           
    //浠庡簳閮ㄤ笂鍗囩殑閬僵鏁堟灉寮€濮�
    $(".con").hover(function(){
        $(this).find(".txt").stop().animate({height:"198px"},200);
        $(this).find(".txt h3").stop().animate({paddingTop:"60px"},200);
    },function(){
        $(this).find(".txt").stop().animate({height:"45px"},200);
        $(this).find(".txt h3").stop().animate({paddingTop:"0px"},200);
    })
    //浠庡簳閮ㄤ笂鍗囩殑閬僵鏁堟灉缁撴潫
    
    
    //鐩存帴鏄剧ず閬僵鏁堟灉寮€濮�
    $(".con-two").hover(function(){
        $(this).find(".txt-two").css("display","block");
        },function(){
            $(this).find(".txt-two").css("display","none");
    })
    //鐩存帴鏄剧ず閬僵鏁堟灉缁撴潫
    
    
    //浠庡乏涓婇儴鏄剧ず閬僵鏁堟灉 寮€濮�
    $(".con-three").hover(function() {
        $(this).find(".txt-three").stop().animate({"left": 0,"top":0});
    }, function() {
        $(this).find(".txt-three").stop().animate({"left":-297,"top":-198});
    })
    //浠庡乏涓婇儴鏄剧ず閬僵鏁堟灉 缁撴潫
    
    
    //浠庡乏渚ф樉绀洪伄缃╂晥鏋� 寮€濮�
    $(".con-four").hover(function() {
        $(this).find(".txt-four").stop().animate({"left": 0});
    }, function() {
        $(this).find(".txt-four").stop().animate({"left":-297});
    })
    //浠庡乏渚ф樉绀洪伄缃╂晥鏋� 缁撴潫
    
    
    //鍥剧墖鏀惧ぇ鏁堟灉 寮€濮�
    $(".con-five").hover(function() {
        $(this).find(".conimg").stop().animate({"width":310,"height":210});
    }, function() {
        $(this).find(".conimg").stop().animate({"width":297,"height":198});
    })
    //鍥剧墖鏀惧ぇ鏁堟灉 缁撴潫
    
    
    //鍥剧墖鏀惧ぇ鏁堟灉浼撮殢钂欑増鏂囧瓧鍑虹幇 寮€濮�
    $(".con-six").hover(function() {
        $(this).find(".conimg-two").stop().animate({"width":310,"height":210});
        $(this).find(".txt-six").css("display","block");
    }, function() {
        $(this).find(".conimg-two").stop().animate({"width":297,"height":198});
        $(this).find(".txt-six").css("display","none");
    })
    //鍥剧墖鏀惧ぇ鏁堟灉浼撮殢钂欑増鏂囧瓧鍑虹幇 缁撴潫
    
});

window.onload = function (){
	/*-----------下拉菜单---------*/
	//1. 获取元素节点
	var currentAddr = document.getElementsByClassName('currentAddress')[0];
	var select = document.getElementsByClassName('select')[0];
	//获取内层列表中地址项
	var address = select.children;
	//为每一项添加点击事件
	for(var i = 0; i < address.length; i ++){
		address[i].onclick = function(){
			//传值
			currentAddr.innerHTML = this.innerHTML;
		};
	}
	/*-----------图片轮播-----------*/
	//1. 获取图片数组
	//2. 定时器实现图片切换
	//3. 图片切换主要切换数组下标，防止数组越界
	var banner = document.getElementsByClassName('wrapper')[0];
	var imgs = banner.children; //图片数组
	var imgNav = document.getElementsByClassName('imgNav')[0];
	var indInfo = imgNav.children; //索引数组
	var imgIndex = 0; //初始下标
	var timer;
	timer = setInterval(autoPlay,1000); //定时器
	function autoPlay(){
		//设置元素隐藏与显示
		imgs[imgIndex].style.display = "none";
		/*
		++ imgIndex;
		if(imgIndex == imgs.length){
			imgIndex = 0;
		}
		*/
		imgIndex = ++ imgIndex == imgs.length ? 0 : imgIndex;
		imgs[imgIndex].style.display = "block";
		for(var i = 0; i < indInfo.length; i ++){
			indInfo[i].style.background = "gray";
		}
		//切换索引 切换背景色
		indInfo[imgIndex].style.background = "red";
	}
	banner.onmouseover = function (){
		//停止定时器
		clearInterval(timer);
	};
	banner.onmouseout = function (){
		timer = setInterval(autoPlay,1000);
	};
};



function check_login(){
    $.get('/index/check_login',data,function(data){
        var html=''
        if (data.loginState==0){
            html="<a herf='/index/check_login'>[登录]</a>";
            html+="<a herf='/index/register'>[注册]</a>";
        }else{
            html+="欢迎："+data.username;
            html+="<a herf='/index/check_login'>退出</a>";
        }
        $("#login").html(html)

    },'json');

}


$(function(){


}


)


//<div class="title">
//                <h3 class="fl">礼品卡券</h3>
//                <div class="fr">更多</div>
//                <div class="cb"></div>
//            </div>
//             <ul>
//                <li class="fl">
//                    <div class="box">
//                        <figure>
//                            <img src="/static/imgs/09.jpg" alt="">
//                        </figure>
//                        <div class="tip">
//                            <div class="fl">
//                                <h4>欢乐时光水果</h4>
//                                <p>$188.00/1份</p>
//                            </div>
//                            <div class="fr">
//                                <figure>
//                                    <img src="/static/imgs/cart.png" alt="">
//                                </figure>
//                            </div>
//                            <div class="cb"></div>
//                        </div>
//                    </div>
//                </li>
//







function loadGoods(){
    $.get('/index/load_goods',function(data){
        var show=''
        $.each(data,function(i,obj){
            show+='<div class="title">';
            show+='<h3 class="fl">'+obj.type.title+'</h3>';
            show+='<div class="fr">更多</div>';
            show+='<div class="cb"></div>';
        show+='</div>';
        $.each(obj.goods,function(ix,gobj){
            show+='<li class="fl">';
                show+='';

            show+='</div>';
                show+='<div class="box">';
                    show+='<figure>';
                    show+='<img src="/'+gobj.picture+'">';
                    show+='</figure>';
                show+='<div class="tip">';
                show+='<div class="fl">';
                    show+='<h4>'+gobj.title+'</h4>';
                    show+='<p>$'+gobj.price+'/'+gobj.spec+'</p>';
                show+='</div>';
                show+='<div class="fr">';
                    show+='<figure>';
                        show+='<img src="/static/imgs/cart.png">';
                    show+='</figure>';
                show+='</div>';
            show+='</div>';
        show+='</div>';
    show+='</li>';






        });
        show+='</ul>'
        });
        $('#main')

    },'json');

}

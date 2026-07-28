(function($) {
    "use strict";

    var $window = $(window);
    var $body = $('body');

    /* Preloader Effect */
    $window.on('load', function() {
        $(".preloader").fadeOut(600);
    });

    /* Sticky Header */
    if ($('.active-sticky-header').length) {
        $window.on('resize', function() {
            setHeaderHeight();
        });

        function setHeaderHeight() {
            $("header.active-sticky-header").css("height", $('header.active-sticky-header .header-sticky').outerHeight());
        }

        $window.on("scroll", function() {
            var fromTop = $(window).scrollTop();
            setHeaderHeight();
            var headerHeight = $('header.active-sticky-header .header-sticky').outerHeight()
            $("header.active-sticky-header .header-sticky").toggleClass("hide", (fromTop > headerHeight + 100));
            $("header.active-sticky-header .header-sticky").toggleClass("active", (fromTop > 600));
        });
    }

    if ($("a[href='#top']").length) {
        $(document).on("click", "a[href='#top']", function() {
            $("html, body").animate({
                scrollTop: 0
            }, "slow");
            return false;
        });
    }

    /* testimonial Slider JS */
    if ($('.testimonial-slider').length) {
        const testimonial_slider = new Swiper('.testimonial-slider .swiper', {
            slidesPerView: 1,
            speed: 1000,
            spaceBetween: 30,
            loop: true,
            autoplay: {
                delay: 5000,
            },
            pagination: {
                el: '.testimonial-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.testimonial-button-next',
                prevEl: '.testimonial-button-prev',
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                },
                1025: {
                    slidesPerView: 3,
                },
                1441: {
                    slidesPerView: 4,
                }
            }
        });
    }

    /* Hero Company Support Slider Prime JS */
    if ($('.hero-company-supports-slider-prime').length) {
        const hero_company_supports_slider_prime = new Swiper('.hero-company-supports-slider-prime .swiper', {
            slidesPerView: 2,
            speed: 2000,
            spaceBetween: 30,
            loop: true,
            autoplay: {
                delay: 5000,
            },
            breakpoints: {
                768: {
                    slidesPerView: 3,
                },
                991: {
                    slidesPerView: 4,
                },
                1441: {
                    slidesPerView: 5,
                },
            }
        });
    }

    /* testimonial Slider Prime JS */
    if ($('.testimonial-slider-prime').length) {
        const testimonial_slider_prime = new Swiper('.testimonial-slider-prime .swiper', {
            slidesPerView: 1,
            speed: 1000,
            spaceBetween: 20,
            loop: true,
            autoplay: {
                delay: 5000,
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                },
                1440: {
                    slidesPerView: 3,
                },
            }
        });
    }

    /* testimonial Slider Royal JS */
    if ($('.testimonial-slider-royal').length) {
        const testimonial_slider_royal = new Swiper('.testimonial-slider-royal .swiper', {
            slidesPerView: 1,
            speed: 1000,
            spaceBetween: 30,
            loop: true,
            autoplay: {
                delay: 5000,
            },
            pagination: {
                el: '.testimonial-pagination-royal',
                clickable: true,
            },
            breakpoints: {
                767: {
                    slidesPerView: 1,
                },
                1440: {
                    slidesPerView: 2,
                }

            }
        });
    }

    /* Skill Bar */
    if ($('.skills-progress-bar').length) {
        $('.skills-progress-bar').waypoint(function() {
            $('.skillbar').each(function() {
                $(this).find('.count-bar').animate({
                    width: $(this).attr('data-percent')
                }, 2000);
            });
        }, {
            offset: '70%'
        });
    }



    /* Init Counter */
    if ($('.counter').length) {
        $('.counter').counterUp({
            delay: 6,
            time: 3000
        });
    }

    /* Image Reveal Animation */
    if ($('.reveal').length) {
        gsap.registerPlugin(ScrollTrigger);
        let revealContainers = document.querySelectorAll(".reveal");
        revealContainers.forEach((container) => {
            let image = container.querySelector("img");
            let tl = gsap.timeline({
                scrollTrigger: {
                    trigger: container,
                    toggleActions: "play none none none"
                }
            });
            tl.set(container, {
                autoAlpha: 1
            });
            tl.from(container, 1, {
                xPercent: -100,
                ease: Power2.out
            });
            tl.from(image, 1, {
                xPercent: 100,
                scale: 1,
                delay: -1,
                ease: Power2.out
            });
        });
    }

    /* Text Effect Animation */
    function initHeadingAnimation() {

        if ($('.text-effect').length) {
            var textheading = $(".text-effect");

            if (textheading.length === 0) return;
            gsap.registerPlugin(SplitText);
            textheading.each(function(index, el) {

                el.split = new SplitText(el, {
                    type: "lines,words,chars",
                    linesClass: "split-line"
                });

                if ($(el).hasClass('text-effect')) {
                    gsap.set(el.split.chars, {
                        opacity: .3,
                        x: "-7",
                    });
                }
                el.anim = gsap.to(el.split.chars, {
                    scrollTrigger: {
                        trigger: el,
                        start: "top 92%",
                        end: "top 60%",
                        markers: false,
                        scrub: 1,
                    },

                    x: "0",
                    y: "0",
                    opacity: 1,
                    duration: .7,
                    stagger: 0.2,
                });

            });
        }

        if ($('.text-anime-style-1').length) {
            let staggerAmount = 0.05,
                translateXValue = 0,
                delayValue = 0.5,
                animatedTextElements = document.querySelectorAll('.text-anime-style-1');

            animatedTextElements.forEach((element) => {
                let animationSplitText = new SplitText(element, {
                    type: "chars, words"
                });
                gsap.from(animationSplitText.words, {
                    duration: 1,
                    delay: delayValue,
                    x: 20,
                    autoAlpha: 0,
                    stagger: staggerAmount,
                    scrollTrigger: {
                        trigger: element,
                        start: "top 85%"
                    },
                });
            });
        }

        if ($('.text-anime-style-2').length) {
            let staggerAmount = 0.03,
                translateXValue = 20,
                delayValue = 0.1,
                easeType = "power2.out",
                animatedTextElements = document.querySelectorAll('.text-anime-style-2');

            animatedTextElements.forEach((element) => {
                let animationSplitText = new SplitText(element, {
                    type: "chars, words"
                });
                gsap.from(animationSplitText.chars, {
                    duration: 1,
                    delay: delayValue,
                    x: translateXValue,
                    autoAlpha: 0,
                    stagger: staggerAmount,
                    ease: easeType,
                    scrollTrigger: {
                        trigger: element,
                        start: "top 85%"
                    },
                });
            });
        }

        if ($('.text-anime-style-3').length) {
            let animatedTextElements = document.querySelectorAll('.text-anime-style-3');

            animatedTextElements.forEach((element) => {
                //Reset if needed
                if (element.animation) {
                    element.animation.progress(1).kill();
                    element.split.revert();
                }

                element.split = new SplitText(element, {
                    type: "lines,words,chars",
                    linesClass: "split-line",
                });
                gsap.set(element, {
                    perspective: 400
                });

                gsap.set(element.split.chars, {
                    opacity: 0,
                    x: "50",
                });

                element.animation = gsap.to(element.split.chars, {
                    scrollTrigger: {
                        trigger: element,
                        start: "top 90%"
                    },
                    x: "0",
                    y: "0",
                    rotateX: "0",
                    opacity: 1,
                    duration: 1,
                    ease: Back.easeOut,
                    stagger: 0.02,
                });
            });
        }
    }

    if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(() => {
            initHeadingAnimation();
        });
    } else {
        window.addEventListener("load", initHeadingAnimation);
    }

    /* Contact form — mailto redirect */
    var $contactform = $("#contactForm");
    if ($contactform.length) {
        $contactform.on("submit", function(e) {
            e.preventDefault();
            var name = $("#name").val().trim();
            var email = $("#email").val().trim();
            var subject = $("#subject").val().trim();
            var message = $("#message").val().trim();
            if (name && email && message) {
                var mailtoLink = "mailto:syafrial@iotaru.com?subject=" + encodeURIComponent(subject || "Contact from " + name) + "&body=" + encodeURIComponent("Name: " + name + "\nEmail: " + email + "\n\n" + message);
                window.open(mailtoLink, "_blank");
                $contactform[0].reset();
                $("#msgSubmit").removeClass().addClass("h4 text-success").text("Opening email client...");
            } else {
                $("#msgSubmit").removeClass().addClass("h4 text-danger").text("Please fill in all fields.");
            }
        });
    }

    /* Animated Wow Js */
    new WOW().init();

    /* Our Pricing Tab JS Start  */
    if ($('.our-pricing-box').length) {
        $('#planToggle').change(function() {
            if ($(this).is(':checked')) {
                $('#monthly').addClass('d-none');
                $('#yearly').removeClass('d-none');
            } else {
                $('#yearly').addClass('d-none');
                $('#monthly').removeClass('d-none');
            }
        });
    }
    /* Our Pricing Tab JS End  */


    /* About US Item List Start */
    var $about_us_item_list_prime = $('.about-us-item-list-prime');
    if ($about_us_item_list_prime.length) {
        var $about_us_item_prime = $about_us_item_list_prime.find('.about-us-item-prime');

        if ($about_us_item_prime.length) {
            $about_us_item_prime.on({
                mouseenter: function() {
                    if (!$(this).hasClass('active')) {
                        $about_us_item_prime.removeClass('active');
                        $(this).addClass('active');
                    }
                },
                mouseleave: function() {
                    // Optional: Add logic for mouse leave if needed
                }
            });
        }
    }
    /* About US Item List End */

})(jQuery);
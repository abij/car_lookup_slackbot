from unittest import mock, TestCase

from slackbot.finnik import FinnikOnlineClient

FINNIK_RES_DATA = """
<html lang="nl" class="no-touch"><head prefix="og: http://ogp.me/ns#">
        

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>H-532-DT - BMW i3 - Finnik Kentekencheck - Finnik.nl</title>
    <meta name="description" content="Meest gebruikte kentekencheck van Nederland. >160,000 rapporten per dag. Check nu voertuiggegevens, wegenbelasting, eigenarenhistorie en veel meer. ">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta property="og:locale" content="nl">
<meta property="og:type" content="website">
    <meta property="og:title" content="H-532-DT - Alles over de BMW i3 Executive Edition 120Ah 42 kWh">
    <meta property="og:description" content="Ik heb de BMW i3 Executive Edition 120Ah 42 kWh uit 2019 gespot op Finnik.">
<meta property="og:url" content="https://finnik.nl/kenteken/h532dt/gratis">
<meta property="og:site_name" content="Finnik.nl">
<meta property="article:publisher" content="https://www.facebook.com/finnik.nl/">
<meta property="og:image" content="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_F2.jpg">
<meta property="og:image:width" content="1160">
<meta property="og:image:height" content="510">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@finnikNL">
<meta name="apple-itunes-app" content="app-id=451526873, app-argument=finnik://finnik.com/licenseplate/h532dt">
<meta name="theme-color" content="#00ada8">
<link rel="manifest" href="/content/manifest.json" crossorigin="use-credentials">
<link href="/favicon.ico" rel="shortcut icon" type="image/x-icon">
<meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
<link href="/content/assets/favicon.ico" rel="shortcut icon" type="image/x-icon">
<link rel="stylesheet" href="/content/css/libraries.min.css">

    
    
        <link rel="stylesheet" href="/content/css/finnik/pages/carReport.min.css?v=100492">
    
    <link rel="stylesheet" href="/content/css/dark.css">
    <link rel="stylesheet" media="print" href="/content/css/print.min.css">
<script async="" src="https://connect.facebook.net/en_US/fbevents.js"></script><script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script type="text/javascript" defer="" src="https://www.google-analytics.com/plugins/ua/ec.js"></script>
<script type="text/javascript" defer="" src="https://www.google-analytics.com/analytics.js"></script>
<script type="text/javascript" defer="" src="//www.googleadservices.com/pagead/conversion_async.js"></script>
<script defer="" src="https://www.googletagmanager.com/gtm.js?id=GTM-W63PLG"></script>

<script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4962815710377677" crossorigin="anonymous"></script>

        
        
    <script src="https://www.googletagmanager.com/gtag/js?l=dataLayer&amp;id=G-9GJ492V4LW" async=""></script><style type="text/css">.TnITTtw-fp-collapsed-button {
    display: none;
    position: fixed !important;
    top: 16px !important;
    right: 16px !important;
}

.TnITTtw-fp-collapsed-button:hover {
    opacity: 1.0 !important;
}

.TnITTtw-mate-fp-bar {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica, Arial, Ubuntu, sans-serif !important;
    color: #000;
    position: fixed;
    top: 16px;
    right: 16px;
    z-index: 999;
    background: rgb(255 255 255 / 0.95);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 16px;
    border-radius: 11px;
    box-shadow: 0 2px 10px rgb(0 0 0 / 25%);
    width: 320px;
    line-height: initial;
}

@-moz-document url-prefix() {
    .TnITTtw-mate-fp-bar {
        background: rgb(255 255 255 / 1.0);
    }
}

.TnITTtw-mate-fp-bar.TnITTtw-dark-mode {
    background: rgb(44, 44, 43);
}

.TnITTtw-hide-fp-bar {
    width: 12px;
    height: 12px;
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/regular-close-tt.png) !important;
    background-size: 12px 12px;
    background-repeat: no-repeat;
    background-position: center;
    position: absolute;
    right: 8px;
    top: 8px;
    cursor: pointer;
}

.TnITTtw-hide-fp-bar:hover {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/hover-close-tt.png) !important;
}

.TnITTtw-current-page-lang {
    color: #6d6d72;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 8px;
    text-align: center;
}

.TnITTtw-dark-mode .TnITTtw-current-page-lang {
    color: #98989D;
}

.TnITTtw-fp-translate {
    width: calc(100% - 73px) !important;
    font-size: 14px !important;
    text-transform: none !important;
}

.TnITTtw-fp-translate.TnITTtw-in-progress {
    animation-name: funky-bg;
    animation-duration: 10s;
    animation-timing-function: ease-in;
}

.TnITTtw-fp-translate.TnITTtw-show-original {
    width: calc(100% - 20px) !important;
}

@keyframes funky-bg {
    from {
        background-image: linear-gradient(145deg, #01EF92, #00D8FB),
        linear-gradient(35deg, rgba(1, 239, 146, 0.25), rgba(0, 216, 251, 0.25)) !important;
    }

    to {
        background-image: linear-gradient(90deg, #01EF92, #00D8FB),
        linear-gradient(35deg, rgba(1, 239, 146, 0.25), rgba(0, 216, 251, 0.25)) !important;
    }
}

.TnITTtw-change-language, .TnITTtw-stop-fp {
    width: 38px;
    height: 38px;
    background-color: #EFEFF4;
    background-repeat: no-repeat;
    background-position: center;
    background-size: 16px 16px;
    border-radius: 11px;
    display: inline-block;
    vertical-align: top;
    cursor: pointer;
}

.TnITTtw-change-language {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/globe-earth.png) !important;
}

.TnITTtw-dark-mode .TnITTtw-change-language {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/globe-earth-dark.png) !important;
}

.TnITTtw-stop-fp {
    display: none;
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/regular-stt-stop.png) !important;
    background-size: 12px 12px;
}

.TnITTtw-dark-mode .TnITTtw-change-language, .TnITTtw-dark-mode .TnITTtw-stop-fp {
    background-color: #525251 !important;
}

.TnITTtw-change-language:hover, .TnITTtw-stop-fp:hover {
    background-color: #F6F6F6;
}

.TnITTtw-change-language:active, .TnITTtw-stop-fp:active {
    background-color: #E9E9E9;
}

.TnITTtw-dark-mode .TnITTtw-change-language:hover,
.TnITTtw-dark-mode .TnITTtw-stop-fp:hover,
.TnITTtw-dark-mode .TnITTtw-change-language:active,
.TnITTtw-dark-mode .TnITTtw-stop-fp:active {
    background-color: #767675;
}

#TnITTtw-always-translate {
}

.TnITTtw-fp-options input {
    padding: initial;
    width: auto;
    border: initial;
    box-shadow: initial;
    line-height: initial;
    height: auto;
    display: initial;
    position: initial;
    appearance: auto;
    top: initial;
    cursor: pointer;
    margin: 0;
}

.TnITTtw-fp-options input[readonly="readonly"] {
    opacity: 0.5;
}

#TnITTtw-always-translate + label,
#TnITTtw-never-translate-lang + label,
#TnITTtw-never-translate-site + label {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica, Arial, Ubuntu, sans-serif !important;
    display: inline-block;
    font-weight: 400;
    font-size: 14px;
    margin-left: 4px;
    color: #000;
    cursor: pointer;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    width: 296px;
    vertical-align: top;
    line-height: initial;
    letter-spacing: initial;
    text-transform: initial;
    margin-right: 0;
    margin-top: 0;
    margin-bottom: 0;
    padding: 0;
}

#TnITTtw-always-translate + label::before,
#TnITTtw-never-translate-lang + label::before,
#TnITTtw-never-translate-site + label::before,
#TnITTtw-always-translate + label::after,
#TnITTtw-never-translate-lang + label::after,
#TnITTtw-never-translate-site + label::after  {
    content: initial;
} 

.TnITTtw-always-translate-inner-label {
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    max-width: 252px;
    vertical-align: top;
    display: inline-block;
}

.TnITTtw-dark-mode #TnITTtw-always-translate + label,
.TnITTtw-dark-mode #TnITTtw-never-translate-lang + label,
.TnITTtw-dark-mode #TnITTtw-never-translate-site + label {
    color: #FFF;
}

#TnITTtw-always-translate + label.TnITTtw-not-pro {
    opacity: 0.5;
}

#TnITTtw-always-translate + label .TnITTtw-pro-label {
    position: relative;
    background: #000;
    font-size: 11px;
    text-transform: uppercase;
    color: #FFF;
    padding: 2px 5px;
    border-radius: 4px;
    margin-left: 10px;
    top: -1px;
    user-select: none;
    -webkit-user-select: none;
    display: inline;
    font-weight: 500;
}

.TnITTtw-dark-mode #TnITTtw-always-translate + label .TnITTtw-pro-label {
    background: #FFF;
    color: #000;
}

.TnITTtw-inline-original-tooltip {
    display: none;
    position: absolute;
    margin: 0px;
    border: none;
    padding: 16px;
    color: rgb(0, 0, 0);
    background-color: rgb(255 255 255 / 0.95);
    backdrop-filter: blur(10px);
    border-radius: 11px;
    box-shadow: 0 2px 10px rgb(0 0 0 / 25%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica, Arial, Ubuntu, sans-serif;
    font-style: normal;
    font-variant: normal;
    font-weight: normal;
    font-size: 16px;
    line-height: normal;
}

.TnITTtw-dark-mode.TnITTtw-inline-original-tooltip {
    background-color: rgb(0 0 0 / 0.915);
    color: #FFF;
}

.TnITTtw-inline-original-tooltip .TnITTtw-close-original-tooltip {
    width: 12px;
    height: 12px;
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/regular-close-tt.png) !important;
    background-size: 12px 12px;
    background-repeat: no-repeat;
    background-position: center;
    position: absolute;
    right: 8px;
    top: 8px;
    cursor: pointer;
}

.TnITTtw-inline-original-tooltip .TnITTtw-close-original-tooltip:hover {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/hover-close-tt.png) !important;
}

.TnITTtw-inline-original-tooltip .TnITTtw-original-label {
    margin: 0;
    font-weight: 600;
    font-size: 13px;
    text-transform: uppercase;
    color: #6d6d72;
    margin-bottom: 10px;
}

.TnITTtw-inline-original-tooltip.TnITTtw-dark-mode .TnITTtw-original-label {
    color: #98989D;
}

.TnITTtw-inline-original-tooltip .TnITTtw-text-layout {
    display: inline-block;
    margin: 0;
    font-size: 16px;
    color: #000;
}

.TnITTtw-inline-original-tooltip.TnITTtw-dark-mode .TnITTtw-text-layout {
    color: #FFF;
}

.TnITTtw-highlighted-for-original {
    color: #0F0F5F;
    background-color: #F0F0A0;
}

/* Dropdown scrollbars */

#selVisibleScroll-1, #selVisibleScroll-2, #selVisibleScroll-3 {
    overflow: hidden;
    height: 259px;
    width: 100%;
    position: relative;
}

#sel-scrollbar-1, #sel-scrollbar-2, #sel-scrollbar-3 {
    position: absolute;
    width: 4px;
    height: 259px;
    left: 225px;
}

#sel-track-1, #sel-track-2, #sel-track-3 {
    position: absolute;
    top: 1px;
    width: 4px;
    height: calc(100% - 6px);
}

#sel-dragBar-1, #sel-dragBar-2, #sel-dragBar-3 {
    position: absolute;
    top: 1px;
    width: 4px;
    background: rgba(43, 43, 43, 0.5);
    cursor: pointer;
    border-radius: 4px;
}

.dark-mode #sel-dragBar-1, .dark-mode #sel-dragBar-2, .dark-mode #sel-dragBar-3 {
    background: rgba(255, 255, 255, 0.5);
}

#sel-dragBar-1:hover, #sel-dragBar-2:hover, #sel-dragBar-3:hover, 
#sel-dragBar-1:active, #sel-dragBar-2:active, #sel-dragBar-3:active {
    background: rgba(43, 43, 43, 0.675);
}

.dark-mode #sel-dragBar-1:hover,
.dark-mode #sel-dragBar-2:hover,
.dark-mode #sel-dragBar-3:hover,
.dark-mode #sel-dragBar-1:active,
.dark-mode #sel-dragBar-2:active,
.dark-mode #sel-dragBar-3:active {
    background: rgba(255, 255, 255, 0.675);
}

#sel-scrollbar-1, #sel-track-1, #sel-dragBar-1, 
#sel-scrollbar-2, #sel-track-2, #sel-dragBar-2,
#sel-scrollbar-3, #sel-track-3, #sel-dragBar-3 {
    -webkit-user-select: none;
    user-select: none;
}

/* Spinner for when it's translating a page */

.TnITTtw-cta-button-layout {
    position: relative;
    display: inline;
}

.TnITTtw-spinner {
    display: none;
    text-align: center;
    position: absolute;
    top: 0;
    width: 100%;
    user-select: none;
    -webkit-user-select: none;
}
  
  @media screen and (max-width: 800px) {
    .TnITTtw-spinner {
      top: 28px;
    }
  }

  .TnITTtw-spinner.in-text {
    display: block;
    background: transparent;
    position: initial;
  }

  .TnITTtw-spinner.left {
    text-align: left;
  }
  
  .TnITTtw-spinner > div {
    width: 12px;
    height: 12px;
    background-color: rgb(0, 71, 46);
  
    border-radius: 100%;
    display: inline-block;
    -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
    animation: sk-bouncedelay 1.4s infinite ease-in-out both;
  }

  .TnITTtw-spinner.in-text > div {
    background-color: #000;
  }
  
  .TnITTtw-spinner .TnITTtw-bounce1 {
    -webkit-animation-delay: -0.32s;
    animation-delay: -0.32s;
  }
  
  .TnITTtw-spinner .TnITTtw-bounce2 {
    -webkit-animation-delay: -0.16s;
    animation-delay: -0.16s;
  }
  
  @-webkit-keyframes sk-bouncedelay {
    0%, 80%, 100% { -webkit-transform: scale(0) }
    40% { -webkit-transform: scale(1.0) }
  }
  
  @keyframes sk-bouncedelay {
    0%, 80%, 100% { 
      -webkit-transform: scale(0);
      transform: scale(0);
    } 40% { 
      -webkit-transform: scale(1.0);
      transform: scale(1.0);
    }
  }</style><style type="text/css">/*
 * contextMenu.js v 1.4.0
 * Author: Sudhanshu Yadav
 * s-yadav.github.com
 * Copyright (c) 2013 Sudhanshu Yadav.
 * Dual licensed under the MIT and GPL licenses
**/

.iw-contextMenu {
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.10) !important;
    border: 1px solid #c8c7cc !important;
    border-radius: 11px !important;
    display: none;
    z-index: 1000000132;
    max-width: 300px !important;
    width: auto !important;
}

.dark-mode .iw-contextMenu,
.TnITTtw-dark-mode.iw-contextMenu,
.TnITTtw-dark-mode .iw-contextMenu {
    border-color: #747473 !important;
}

.iw-cm-menu {
    background: #fff !important;
    color: #000 !important;
    margin: 0px !important;
    padding: 0px !important;
    overflow: visible !important;
}

.dark-mode .iw-cm-menu,
.TnITTtw-dark-mode.iw-cm-menu,
.TnITTtw-dark-mode .iw-cm-menu {
    background: #525251 !important;
    color: #FFF !important;
}

.iw-curMenu {
}

.iw-cm-menu li {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica, Arial, Ubuntu, sans-serif !important;
    list-style: none !important;
    padding: 10px !important;
    padding-right: 20px !important;
    border-bottom: 1px solid #c8c7cc !important;
    font-weight: 400 !important;
    cursor: pointer !important;
    position: relative !important;
    font-size: 14px !important;
    margin: 0 !important;
    line-height: inherit !important;
    border-radius: 0 !important;
    display: block !important;
}

.dark-mode .iw-cm-menu li, .TnITTtw-dark-mode .iw-cm-menu li {
    border-bottom-color: #747473 !important;
}

.iw-cm-menu li:first-child {
    border-top-left-radius: 11px !important;
    border-top-right-radius: 11px !important;
}

.iw-cm-menu li:last-child {
    border-bottom-left-radius: 11px !important;
    border-bottom-right-radius: 11px !important;
    border-bottom: none !important;
}

.iw-mOverlay {
    position: absolute !important;
    width: 100% !important;
    height: 100% !important;
    top: 0px !important;
    left: 0px !important;
    background: #FFF !important;
    opacity: .5 !important;
}

.iw-contextMenu li.iw-mDisable {
    opacity: 0.3 !important;
    cursor: default !important;
}

.iw-mSelected {
    background-color: #F6F6F6 !important;
}

.dark-mode .iw-mSelected, .TnITTtw-dark-mode .iw-mSelected {
    background-color: #676766 !important;
}

.iw-cm-arrow-right {
    width: 0 !important;
    height: 0 !important;
    border-top: 5px solid transparent !important;
    border-bottom: 5px solid transparent !important;
    border-left: 5px solid #000 !important;
    position: absolute !important;
    right: 5px !important;
    top: 50% !important;
    margin-top: -5px !important;
}

.dark-mode .iw-cm-arrow-right, .TnITTtw-dark-mode .iw-cm-arrow-right {
    border-left-color: #FFF !important;
}

.iw-mSelected > .iw-cm-arrow-right {
}

/*context menu css end */</style><style type="text/css">.ui_selector, .TnITTtw-ui_selector {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica, Arial, Ubuntu, sans-serif;
    display: inline-block;
}

.ui_selector .select, .TnITTtw-ui_selector .TnITTtw-select {
    color: #000;
    text-align: center;
    font-weight: 600;
    font-size: 14px;
    border: 1px solid rgba(200, 199, 204, 0.5);
    padding: 10px 15px;
    width: 201px;
    -webkit-user-select: none;
    cursor: pointer;
    border-radius: 11px;
    display: inline-block;
    background-image: -webkit-linear-gradient(top, #FAFAFA, #F6F6F6);
    background-image: -moz-linear-gradient(top, #FAFAFA, #F6F6F6);
    background-size: auto 48px;
    background-position: 0px -11px;
    box-shadow: 0 0.5px 1px rgba(0, 0, 0, 0.10);
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
}

.dark-mode .ui_selector .select, 
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-select {
    background-image: -webkit-linear-gradient(top, #4A4A49, #40403F);
    background-image: -moz-linear-gradient(top, #4A4A49, #40403F);
    color: #FFF;
    border-color: #747473;
}

.ui_selector .select:hover,
.TnITTtw-ui_selector .TnITTtw-select:hover {
    color: #424242;
    background-image: -webkit-linear-gradient(top, #FAFAFA, #FAFAFA);
    background-image: -moz-linear-gradient(top, #FAFAFA, #FAFAFA);
}

.ui_selector .select:active,
.TnITTtw-ui_selector .TnITTtw-select:active {
    color: #6d6d72;
    background-image: -webkit-linear-gradient(top, #F6F6F6, #F6F6F6);
    background-image: -moz-linear-gradient(top, #F6F6F6, #F6F6F6);
}

.dark-mode .ui_selector .select:hover,
.dark-mode .ui_selector .select:active,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-select:hover,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-select:active {
    background-image: -webkit-linear-gradient(top, #4A4A49, #4A4A49);
    background-image: -moz-linear-gradient(top, #4A4A49, #4A4A49);
    color: #FFF;
    border-color: #747473;
}

.ui_selector .select .detected-ico,
.TnITTtw-ui_selector .TnITTtw-select .TnITTtw-detected-ico {
    display: inline-block;
}

.ui_selector .active, .ui_selector .active:hover, .ui_selector .active:active,
.TnITTtw-ui_selector .TnITTtw-active, .TnITTtw-ui_selector .TnITTtw-active:hover, .TnITTtw-ui_selector .TnITTtw-active:active {
    box-shadow: 0 -1px 15px -10px rgba(0, 0, 0, 0.85) !important;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    background: #F3F3F3;
}

.sliding-text,
.TnITTtw-sliding-text {
    position: relative;
}

.ui_selector .options,
.TnITTtw-ui_selector .TnITTtw-options {
    margin-left: 0px;
    margin-top: -4px;
    background: #fff;
    border: 1px solid rgba(200, 199, 204, 0.5);
    width: 231px;
    overflow: hidden;
    max-height: 313px;
    position: absolute;
    font-size: 12px;
    box-shadow: 0 2px 10px rgb(0 0 0 / 25%);
    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 6px;
    display: none;
}

.ui_selector .options.standalone,
.TnITTtw-ui_selector .TnITTtw-options.TnITTtw-standalone {
    border-radius: 11px;
    margin-top: 16px;
}

/* for now, it can only be on the top */
.ui_selector .options-arrow,
.TnITTtw-ui_selector .TnITTtw-options-arrow {
    display: none;
    position: absolute;
    width: 32px !important;
    height: 18px !important;
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/tt-dropdown-arrow.png);
    background-size: 32px 18px;
    transform: rotate(180deg);
    margin-top: -1px;
}

.dark-mode .ui_selector .options-arrow,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-options-arrow {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/tt-dropdown-arrow-dark.png);
}

.dark-mode .ui_selector .options,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-options {
    background: #525251;
}

.ui_selector .options ul,
.TnITTtw-ui_selector .TnITTtw-options ul {
    list-style: none;
    margin: 0;
    padding: 0;
    width: 232px;
}

.ui_selector .options ul li,
.TnITTtw-ui_selector .TnITTtw-options ul li {
    padding: 10px 0px;
    -webkit-user-select: none;
    text-align: center;
    font-size: 17px;
    -webkit-transition: all 600ms cubic-bezier(0.23, 1, 0.32, 1);
    margin: 0 10px;
    border-radius: 6px;
    position: relative;
}

.dark-mode .options ul li,
.TnITTtw-dark-mode .TnITTtw-options ul li {
    color: #fff;
}

.ui_selector .options ul li:last-child,
.TnITTtw-ui_selector .TnITTtw-options ul li:last-child {
    margin-bottom: 16px;
}

.ui_selector .options ul li.option:first-child,
.ui_selector .options ul li.option_selected:first-child,
.TnITTtw-ui_selector .TnITTtw-options ul li.TnITTtw-option:first-child,
.TnITTtw-ui_selector .TnITTtw-options ul li.TnITTtw-option_selected:first-child {
    margin-top: 16px;
}

.ui_selector .options ul li.whenHover,
.TnITTtw-ui_selector .TnITTtw-options ul li.TnITTtw-whenHover {
    cursor: pointer;
    background: #f3f3f3;
    text-align: center;
}

.dark-mode .ui_selector .options ul li.whenHover,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-options ul li.TnITTtw-whenHover {
    background: rgba(255, 255, 255, 0.5);
}

.ui_selector .options ul li.option_selected,
.TnITTtw-ui_selector .TnITTtw-options ul li.TnITTtw-option_selected {
    cursor: pointer;
    background-image: linear-gradient(145deg, #01EF92, #00D8FB),
    linear-gradient(35deg, rgba(1, 239, 146, 0.25), rgba(0, 216, 251, 0.25)) !important;
    color: #fff;
    font-weight: 600;
}

.ui_selector .options ul .group,
.ui_selector .options ul .group:hover,
.ui_selector .options ul .group.whenHover,
.TnITTtw-ui_selector .TnITTtw-options ul .TnITTtw-group,
.TnITTtw-ui_selector .TnITTtw-options ul .TnITTtw-group:hover,
.TnITTtw-ui_selector .TnITTtw-options ul .TnITTtw-group.whenHover {
    padding: 16px 10px;
    color: #8e8e93;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 12px;
    text-align: center;
    cursor: default;
    background: #FFF;
}

.dark-mode .ui_selector .options ul .group,
.dark-mode .ui_selector .options ul .group:hover,
.dark-mode .ui_selector .options ul .group.whenHover,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-options ul .TnITTtw-group,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-options ul .TnITTtw-group:hover,
.TnITTtw-dark-mode .TnITTtw-ui_selector .TnITTtw-options ul .TnITTtw-group.TnITTtw-whenHover {
    color: #98989D;
    background: #525251;
}

.group-element,
.TnITTtw-group-element {
    width: 153px;
}

.options .dd-search,
.TnITTtw-options .TnITTtw-dd-search {
    border-bottom: 1px solid rgba(200, 199, 204, 0.5);
}

.dark-mode .options .dd-search,
.TnITTtw-dark-mode .TnITTtw-options .TnITTtw-dd-search {
    border-bottom-color: #747473;
}

.dd-search .dd-input,
.TnITTtw-dd-search .TnITTtw-dd-input {
    padding: 16px;
    padding-left: calc(16px * 3);
    width: 168px;
    border: none;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica, Arial, Ubuntu, sans-serif;
    text-align: left;
    color: #000;
    font-size: 17px;
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/searchfield-icon.png);
    background-position: 16px;
    background-size: 16px;
    background-repeat: no-repeat;
    margin: 0;
    height: auto;
}

.dark-mode .dd-search .dd-input,
.TnITTtw-dark-mode .TnITTtw-dd-search .TnITTtw-dd-input {
    color: #FFF;
    background-color: #525251;
}

.dd-search .dd-input:focus,
.TnITTtw-dd-search .TnITTtw-dd-input:focus {
    -webkit-transition: all 275ms cubic-bezier(0.23, 1, 0.32, 1);
    outline: none;
    text-align: left;
}

.dd-input::-webkit-input-placeholder,
.TnITTtw-dd-input::-webkit-input-placeholder {
    color: #8e8e93;
}

.search-failed-plaque,
.TnITTtw-search-failed-plaque {
    text-align: center;
    padding: 20px;
    color: #8e8e93;
    font-size: 17px;
    font-weight: 600;
}

.dark-mode .search-failed-plaque,
.TnITTtw-dark-mode .TnITTtw-search-failed-plaque {
    color: #98989D;
}

.rm-recent,
.TnITTtw-rm-recent {
    position: absolute;
    width: 10px;
    height: 10px;
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/regular-lang-remove.png);
    background-size: 10px 10px;
    top: 15px;
    right: 10px;
}

.rm-recent:hover,
.TnITTtw-rm-recent:hover {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/hover-lang-remove.png);
}

.rm-recent:active,
.TnITTtw-rm-recent:active {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/down-lang-remove.png);
}

.option_selected .rm-recent,
.TnITTtw-option_selected .TnITTtw-rm-recent {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/down-active-lang-remove.png);
}

.option_selected .rm-recent:hover,
.TnITTtw-option_selected .TnITTtw-rm-recent:hover {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/hover-active-lang-remove.png);
}

.option_selected .rm-recent:active,
.TnITTtw-option_selected .TnITTtw-rm-recent:active {
    background-image: url(chrome-extension://ihmgiclibbndffejedjimfjmfoabpcke/res/images/ui/down-active-lang-remove.png);
}

.TnITTtw-hidden {
    display: none;
}</style><style type="text/css">@-webkit-keyframes load4 {
    0%,
    100% {
        box-shadow: 0 -3em 0 0.2em, 2em -2em 0 0em, 3em 0 0 -1em, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 -1em, -3em 0 0 -1em, -2em -2em 0 0;
    }
    12.5% {
        box-shadow: 0 -3em 0 0, 2em -2em 0 0.2em, 3em 0 0 0, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 -1em, -3em 0 0 -1em, -2em -2em 0 -1em;
    }
    25% {
        box-shadow: 0 -3em 0 -0.5em, 2em -2em 0 0, 3em 0 0 0.2em, 2em 2em 0 0, 0 3em 0 -1em, -2em 2em 0 -1em, -3em 0 0 -1em, -2em -2em 0 -1em;
    }
    37.5% {
        box-shadow: 0 -3em 0 -1em, 2em -2em 0 -1em, 3em 0em 0 0, 2em 2em 0 0.2em, 0 3em 0 0em, -2em 2em 0 -1em, -3em 0em 0 -1em, -2em -2em 0 -1em;
    }
    50% {
        box-shadow: 0 -3em 0 -1em, 2em -2em 0 -1em, 3em 0 0 -1em, 2em 2em 0 0em, 0 3em 0 0.2em, -2em 2em 0 0, -3em 0em 0 -1em, -2em -2em 0 -1em;
    }
    62.5% {
        box-shadow: 0 -3em 0 -1em, 2em -2em 0 -1em, 3em 0 0 -1em, 2em 2em 0 -1em, 0 3em 0 0, -2em 2em 0 0.2em, -3em 0 0 0, -2em -2em 0 -1em;
    }
    75% {
        box-shadow: 0em -3em 0 -1em, 2em -2em 0 -1em, 3em 0em 0 -1em, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 0, -3em 0em 0 0.2em, -2em -2em 0 0;
    }
    87.5% {
        box-shadow: 0em -3em 0 0, 2em -2em 0 -1em, 3em 0 0 -1em, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 0, -3em 0em 0 0, -2em -2em 0 0.2em;
    }
}

@keyframes load4 {
    0%,
    100% {
        box-shadow: 0 -3em 0 0.2em, 2em -2em 0 0em, 3em 0 0 -1em, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 -1em, -3em 0 0 -1em, -2em -2em 0 0;
    }
    12.5% {
        box-shadow: 0 -3em 0 0, 2em -2em 0 0.2em, 3em 0 0 0, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 -1em, -3em 0 0 -1em, -2em -2em 0 -1em;
    }
    25% {
        box-shadow: 0 -3em 0 -0.5em, 2em -2em 0 0, 3em 0 0 0.2em, 2em 2em 0 0, 0 3em 0 -1em, -2em 2em 0 -1em, -3em 0 0 -1em, -2em -2em 0 -1em;
    }
    37.5% {
        box-shadow: 0 -3em 0 -1em, 2em -2em 0 -1em, 3em 0em 0 0, 2em 2em 0 0.2em, 0 3em 0 0em, -2em 2em 0 -1em, -3em 0em 0 -1em, -2em -2em 0 -1em;
    }
    50% {
        box-shadow: 0 -3em 0 -1em, 2em -2em 0 -1em, 3em 0 0 -1em, 2em 2em 0 0em, 0 3em 0 0.2em, -2em 2em 0 0, -3em 0em 0 -1em, -2em -2em 0 -1em;
    }
    62.5% {
        box-shadow: 0 -3em 0 -1em, 2em -2em 0 -1em, 3em 0 0 -1em, 2em 2em 0 -1em, 0 3em 0 0, -2em 2em 0 0.2em, -3em 0 0 0, -2em -2em 0 -1em;
    }
    75% {
        box-shadow: 0em -3em 0 -1em, 2em -2em 0 -1em, 3em 0em 0 -1em, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 0, -3em 0em 0 0.2em, -2em -2em 0 0;
    }
    87.5% {
        box-shadow: 0em -3em 0 0, 2em -2em 0 -1em, 3em 0 0 -1em, 2em 2em 0 -1em, 0 3em 0 -1em, -2em 2em 0 0, -3em 0em 0 0, -2em -2em 0 0.2em;
    }
}</style><style type="text/css">/* This is not a zero-length file! */</style></head>
    <body id="carReport" class="" data-theme="" style="">
        <!-- Google Tag Manager (noscript) -->
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W63PLG" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        <!-- End Google Tag Manager (noscript) -->

        
    <div id="message" class="hidden">
        <span></span>
        <a href="#" class="dismiss">Sluiten</a>
    </div>


 
<nav class="navbar navbar-expand-lg navbar-light bg-primarycolor">
    <div class="container">
        <a class="navbar-brand mr-sm-5" href="/">
            <img src="/content/assets/logo.svg" loading="lazy" alt="Finnik logo" width="91" height="39">
        </a>
        <button class="navbar-toggler float-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="/">Kentekencheck</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/dagwaarde">Dagwaarde auto</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/kilometercheck">Kilometercheck</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/automarkt">Automarkt</a>
                </li>
            </ul>
            <ul class="navbar-nav navbar-right">
                <li class="nav-item">
<form action="/kenteken/index" class="licenseplateform" data-url="/kenteken/" method="get">                        <div class="input-group">
                            <div class="input-group-append">
                                <input type="text" id="licensePlateNumber" name="licensePlateNumber" class="licenseplateinput form-control-search" placeholder="XX-123-X" maxlength="10" autocomplete="off">
                                <button class="btn-search licenseplatesearch" type="button"></button>
                            </div>
                            <div class="history">
                                <ul>
                                <li><a href="/kenteken/h532td" class="licenseplate" data-event="licenseplate_autofill_history">H-532-TD</a></li><li><a href="/kenteken/65zgxk" class="licenseplate" data-event="licenseplate_autofill_history">65-ZG-XK</a></li><li><a href="/kenteken/hs830v" class="licenseplate" data-event="licenseplate_autofill_history">HS-830-V</a></li></ul>
                            </div>
                        </div>
</form>                </li>
                    <li class="nav-item">
                        <a class="nav-link" data-event="headerLogin" href="/account/login">Mijn Finnik</a>
                    </li>
                <li class="nav-item dropdown-submenu">
                    <a href="#" class="nav-link settings" data-toggle="dropdown"><span class="text">Instellingen</span></a>
                    <ul class="dropdown-menu">       
                        <li><a href="#" class="icon darkmode">Donkere modus</a></li>
                        <li><a class="icon language" href="/setculture?culture=en&amp;returnUrl=%2Fen%2Fkenteken%2Fh532dt%2Fgratis">English</a></li>

                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
<div class="collapse" id="collapseExample">
    <div class="card card-body">
        <div class="container">
            <div class="row">
                <div class="col-sm-3">
                    <h4 class=" mt-2">Wat zoek je precies?</h4>
                </div>
                <div class="col-sm-7">
                    <input type="text" class="form-control">
                </div>
                <div class="col-sm-2">
                    <button class="button">Zoek</button>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    var resourceDarkmode = 'Donkere modus';
    var resourceLightmode = 'Lichte modus';
</script>        

<div class="background">
</div>

    <div class="printonly text-center">
        <img loading="lazy" class="finniklogo" src="/content/icons/finniklogo.svg" alt="Finnik logo"> <br>

        <div class="qrcode"><img src="https://finnik.nl/qr/h532dt" width="200" height="200" class="qr"><br>Bekijk op Finnik.nl</div>
    </div>

<main>
    


<section class="container result" data-sectiontype="summary">
<div class="quickjump fixed" data-origbgimage="url(&quot;https://finnik.nl/svg/summary/405E7A.svg&quot;)">
    Inhoudsopgave
    <div class="quickjumpcontent">
        <ul>
            <li class="top"><a href="#top" class="">Samenvatting</a></li>
        <li><a href="#snellecheck" class="">Snelle check</a></li><li><a href="#technischegegevens" class="">Technische gegevens</a></li><li><a href="#elektrischeinformatie" class="">Elektrische informatie</a></li><li><a href="#historie" class="">Historie</a></li><li><a href="#onderhoudenreparatie" class="">Onderhoud en reparatie</a></li><li><a href="#optiesenaccessoires" class="">Opties en accessoires</a></li><li><a href="#totalekostenpermaand" class="">Totale kosten per maand</a></li><li><a href="#waarde-informatie" class="active">Waarde-informatie</a></li><li><a href="#basisgegevens" class="">Basisgegevens</a></li><li><a href="#milieu" class="">Milieu</a></li><li><a href="#funfacts" class="">Fun Facts</a></li><li><a href="#automarkt" class="">Automarkt</a></li><li><a href="#diefstalcheck" class="">Diefstalcheck</a></li></ul>
    </div>
</div>    <div class="row quickjumpmargin">
        <div class="col-md-6 order-md-12">
            <div class="slider-container">
                    <div id="carouselIndicators" class="carousel slide" data-ride="carousel" data-interval="10000" data-touch="true">
                        <ol class="carousel-indicators">
                                <li data-target="#carouselIndicators" data-slide-to="0" class="active"></li>
                                <li data-target="#carouselIndicators" data-slide-to="1" class=""></li>
                                <li data-target="#carouselIndicators" data-slide-to="2" class=""></li>
                        </ol>
                        <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <a href="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_F2.jpg" data-toggle="lightbox" data-gallery="hidden-images"><img class="d-block w-100" src="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_F2.jpg" alt="BMW i3"></a>
                                </div>
                                <div class="carousel-item">
                                    <a href="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_R2.jpg" data-toggle="lightbox" data-gallery="hidden-images"><img class="d-block w-100" src="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_R2.jpg" alt="BMW i3"></a>
                                </div>
                                <div class="carousel-item">
                                    <a href="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_I2.jpg" data-toggle="lightbox" data-gallery="hidden-images"><img class="d-block w-100" src="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_I2.jpg" alt="BMW i3"></a>
                                </div>
                        </div>
                        <a class="carousel-control-prev" href="#carouselIndicators" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only"></span>
                        </a>
                        <a class="carousel-control-next" href="#carouselIndicators" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only"></span>
                        </a>
                    </div>
            </div>

            <ul class="actions">
                        <li><a class="add" data-event="summaryLogin" href="/account/login" data-origbgimage="url(&quot;https://finnik.nl/svg/add/405E7A.svg&quot;)"><span class="only_desktop">Log in om aan lijst toe te voegen</span><span class="only_mobile">Opslaan</span></a></li>
                        <li><a class="speech" data-event="summaryLogin" href="/account/login" data-origbgimage="url(&quot;https://finnik.nl/svg/speech/405E7A.svg&quot;)"><span class="only_desktop">Log in om een notitie toe te voegen</span><span class="only_mobile">Notitie</span></a></li>
                <li><a href="#" class="share" data-toggle="modal" data-target="#shareModal" data-event="summShare" data-origbgimage="url(&quot;https://finnik.nl/svg/share/405E7A.svg&quot;)"><span class="only_desktop">Deel deze kentekencheck</span><span class="only_mobile">Delen</span></a></li>
                    <li><a href="https://finnik.nl/kenteken/h532dt.pdf" target="_blank" class="download" data-event="downloadPdf" data-origbgimage="url(&quot;https://finnik.nl/svg/download/405E7A.svg&quot;)"><span class="only_desktop">Download rapport als PDF</span><span class="only_mobile">PDF</span></a></li>
            </ul>
        </div>
        <div class="col-md-6 order-md-1">
            <div class="carsummary">
                <h2 class="h1">BMW i3</h2>
                    <h4>Executive Edition 120Ah 42 kWh</h4>

<form action="/kenteken/index" class="licenseplateform" data-url="/kenteken/" method="get">                        <div class="row">
                            <div class="col-12 col-sm-6">
                                <div class="input-group mb-3">
                                    <div class="input-group-append">
                                        <button class="licenseplatesearch btn-search-reverse" type="button" data-event="summSearch">
                                            <img src="/content/assets/glass2.svg" loading="lazy" class="glass" alt="search">
                                        </button>
                                        <input type="text" class="licenseplateinput form-control-search-reverse" placeholder="H-532-DT" value="" maxlength="10">
                                    </div>
                                    <div class="history">
                                        <ul>
                                        <li><a href="/kenteken/h532td" class="licenseplate" data-event="licenseplate_autofill_history">H-532-TD</a></li><li><a href="/kenteken/65zgxk" class="licenseplate" data-event="licenseplate_autofill_history">65-ZG-XK</a></li><li><a href="/kenteken/hs830v" class="licenseplate" data-event="licenseplate_autofill_history">HS-830-V</a></li></ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 col-sm-6 pl-sm-0">
                                <button class="licenseplatesearch button" data-event="summSearch">Zoek kenteken</button>
                            </div>
                        </div>
</form>                <div class="mb-3">
                    

Deze BMW i3 komt uit <strong>2019</strong>, werd geleverd van 01-03-2019 tot 30-08-2021 en kostte toen <strong>€ 46.660,-</strong>. Deze originele Nederlandse personenauto staat sinds 2019 op kenteken, is voorzien van een <strong>elektriciteit-motor</strong>.<br><br>Dit voertuig heeft een maximum vermogen van 125 kW (170 PK), en een continu (elektrisch) vermogen van <strong>75 kW (102 PK)</strong> en een (gecombineerd) verbruik van 13,1 kWh per 100 km.<br><br>De personenauto heeft een topsnelheid van <strong>150 km per uur</strong> en bereikt vanuit stilstand de 100 km/u in 7,3 seconden. De APK is geldig tot 31-12-2023.
                </div>

                    <a href="/checkout/h532dt" class="button col-12 col-sm-8 col-md-8 float-right buypremium noload" data-event="buttonPremium">Bekijk alle data</a>
            </div>
        </div>
    </div>

    
<div class="modal fade" id="shareModal" tabindex="-1" role="dialog" aria-labelledby="shareModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content col-12">
            <div class="modal-header">
                <h2 class="modal-title">Deel deze kentekencheck</h2> <a href="#" class="close" data-dismiss="modal" aria-label="Close"></a>
            </div>
            <div class="modal-body">
                <ul>
                    <li><a target="_blank" href="https://api.whatsapp.com/send?l=en&amp;text=Ik+heb+de+BMW+i3+uit+2019+gespot+op+Finnik.+https%3A%2F%2Ffinnik.nl%2Fkenteken%2Fh532dt%2Fgratis" class="icon whatsapp" data-event="shareWhatsapp">WhatsApp</a></li>
                    <li><a target="_blank" href="https://twitter.com/intent/tweet?text=Ik+heb+de+BMW+i3+uit+2019+gespot+op+Finnik.+https%3A%2F%2Ffinnik.nl%2Fkenteken%2Fh532dt%2Fgratis" class="icon twitter" data-event="shareTwitter">Twitter</a></li>
                    <li><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=finnik.nl/kenteken/h532dt/gratis" class="icon facebook" data-event="shareFacebook">Facebook</a></li>
                    <li><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=finnik.nl/kenteken/h532dt/gratis" class="icon messenger" data-event="shareMessenger" data-origbgimage="url(&quot;https://finnik.nl/svg/messenger/2196f3.svg&quot;)">Messenger</a> </li>
                </ul>

                <label>
                    Link <span class="message"></span><br>
                    <input type="url" value="https://finnik.nl/kenteken/h532dt/gratis" id="copyUrlField" readonly="readonly"> <a href="#" id="copyUrlButton" class="icon copy" data-toggle="tooltip" title="Link kopiëren" data-event="shareCopyUrl" data-origbgimage="url(&quot;https://finnik.nl/svg/copy/405E7A.svg&quot;)"></a> <span id="textCopied">Link gekopieerd!</span>
                </label>
            </div>
            <div class="modal-footer">

            </div>
        </div>
    </div>
</div> 

        <div class="modal fade" id="favouriteModal" tabindex="-1" role="dialog" aria-labelledby="favouriteModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content col-12">
                    <div class="modal-header">
                        <h2 class="modal-title">Favorieten</h2>
                        <span>Aan welke lijsten wilt u de auto toevoegen?</span>
                        <a href="#" class="close" data-dismiss="modal" aria-label="Close"></a>
                    </div>
                    <div class="modal-body">
                    </div>
                    <div class="modal-footer"></div>
                </div>
            </div>
        </div>
        <div class="modal fade" id="noteModal" tabindex="-1" role="dialog" aria-labelledby="noteModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content col-12">
                    <div class="modal-header">
                        <h2 class="modal-title">Voeg een notitie toe</h2>
                        <span>Voeg een persoonlijke notitie toe bij deze auto.</span>
                        <a href="#" class="close" data-dismiss="modal" aria-label="Close"></a>
                    </div>
                    <div class="modal-body">
                        <textarea id="carNoteArea"></textarea>
                        <input type="button" id="saveNoteButton" class="button" value="Opslaan">
                    </div>
                    <div class="modal-footer"></div>
                </div>
            </div>
        </div>
</section>



            <!-- QuickCheck  -->


<section class="result container quickcheck stickytitle">
    <div class="result_title">
        <h3><a id="snellecheck" data-title="Snelle check"></a>Snelle check</h3>
        <p>Waarde-indicatie, onderhoud en meer</p>
    <a href="#" class="backtotop"></a></div>
    <div class="row">
            <div class="col-sm-6 col-md-4 mb-4">
                <div class="icon pricegraph" data-origbgimage="url(&quot;https://finnik.nl/svg/pricegraph/405E7A.svg&quot;)">
                    <h5>Waarde-indicatie</h5>
                    <span>€ 27-32k</span>
                </div>
            </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon garage" data-origbgimage="url(&quot;https://finnik.nl/svg/garage/405E7A.svg&quot;)">
                        <h5>Datum APK</h5>
                        <span>31-12-2023</span>
                    </div>
                </div>
            <div class="col-sm-6 col-md-4 mb-4">
                <div class="icon speed" data-origbgimage="url(&quot;https://finnik.nl/svg/speed/405E7A.svg&quot;)">
                    <h5>0-100 km/u</h5>
                    <span>7,3 sec.</span>
                </div>
            </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon speed" data-origbgimage="url(&quot;https://finnik.nl/svg/speed/405E7A.svg&quot;)">
                        <h5>Topsnelheid</h5>
                        <span>150 km/u</span>
                    </div>
                </div>
            <div class="col-sm-6 col-md-4 mb-4">
                <div class="icon owners" data-origbgimage="url(&quot;https://finnik.nl/svg/owners/405E7A.svg&quot;)">
                    <h5>Aantal eigenaren</h5>
                    <span>0 (1 incl. autobedrijf)</span>
                </div>
            </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon taxi" data-origbgimage="url(&quot;https://finnik.nl/svg/taxi/405E7A.svg&quot;)">
                        <h5>Taxi?</h5>
                        <span>Nee</span>
                    </div>
                </div>
            <div class="col-sm-6 col-md-4 mb-4">
                <div class="icon calendar" data-origbgimage="url(&quot;https://finnik.nl/svg/calendar/405E7A.svg&quot;)">
                    <h5>Bouwjaar</h5>
                    <span>2019</span>
                </div>
            </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon netherlands" data-origbgimage="url(&quot;https://finnik.nl/svg/netherlands/405E7A.svg&quot;)">
                        <h5>Geïmporteerd?</h5>
                        <span>Nee</span>
                    </div>
                </div>
            <div class="col-sm-6 col-md-4 mb-4">
                <div class="icon netherlands" data-origbgimage="url(&quot;https://finnik.nl/svg/netherlands/405E7A.svg&quot;)">
                    <h5>Eerste toelating nationaal</h5>
                    <span>31-12-2019</span>
                </div>
            </div>
    </div>

                <div class="row center">
                        <div class="col-12 col-md-6 text-center">
                        <img src="https://finfabackendprodstorage.blob.core.windows.net/images/autoscout24logo2x1.png" loading="lazy" height="48"> Er zijn 171 auto's van dit type te koop.
                    </div>
                </div>
            <div class="row center">
                <div class="col-12 col-sm-10 col-md-6">
                    
<a href="https://www.autoscout24.nl/lst/BMW/i3?sort=standard&amp;desc=0&amp;cy=NL&amp;utm_source=finnik_app&amp;utm_campaign=buy&amp;utm_medium=co&amp;utm_term=list&amp;utm_content=textbutton" target="_blank" class="button external" data-targethost="autoscout24.nl" data-event="buttonExternal">Koop dit type auto bij AutoScout24</a>
                </div>
            </div>
</section>            <!-- TechnicalData  -->

<section class="result stickytitle" data-sectiontype="TechnicalData">
    <div class="result_title">
        <h3><a id="technischegegevens" data-title="Technische gegevens"></a>Technische gegevens

</h3>
        <p>Vermogen, snelheid, gewicht en meer</p>
    <a href="#" class="backtotop"></a></div>

    




<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Cilinderinhoud</strong><br/>Het totale volume van de verbrandingsruimte van de verbrandingsmotor van het voertuig, uitgedrukt in cm3. Dit wordt geregistreerd voor personenauto's, bedrijfsauto's motorfietsen en bromfietsen.
<span>bron: RDW</span> ">
        Cilinderinhoud
    <span data-toggle="tooltip" data-html="true" title="<strong>Cilinderinhoud</strong><br/>Het totale volume van de verbrandingsruimte van de verbrandingsmotor van het voertuig, uitgedrukt in cm3. Dit wordt geregistreerd voor personenauto's, bedrijfsauto's motorfietsen en bromfietsen.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Cilinderinhoud</strong><br/>Het totale volume van de verbrandingsruimte van de verbrandingsmotor van het voertuig, uitgedrukt in cm3. Dit wordt geregistreerd voor personenauto's, bedrijfsauto's motorfietsen en bromfietsen.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Niet van toepassing

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Topsnelheid
    </div>
    <div class="col-6 col-sm-7 value">
150 km/u

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Aantal cilinders</strong><br/>Het aantal cilinders waarvan de motor van het voertuig is voorzien. Dit wordt geregistreerd voor personenauto's, bedrijfsauto's en motorfietsen.
<span>bron: RDW</span> ">
        Aantal cilinders
    <span data-toggle="tooltip" data-html="true" title="<strong>Aantal cilinders</strong><br/>Het aantal cilinders waarvan de motor van het voertuig is voorzien. Dit wordt geregistreerd voor personenauto's, bedrijfsauto's en motorfietsen.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Aantal cilinders</strong><br/>Het aantal cilinders waarvan de motor van het voertuig is voorzien. Dit wordt geregistreerd voor personenauto's, bedrijfsauto's en motorfietsen.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Niet van toepassing

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Motorcode
    </div>
    <div class="col-6 col-sm-7 value">
IB1P25B

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Vermogen</strong><br/>Dit is de energie die een motor kan leveren om een voertuig in beweging te brengen, uitgedrukt in kW. De RDW registreert dit voor personenauto's, bedrijfsauto's, driewielige motorvoertuigen, motorfietsen en bromfietsen. Vroeger werd het vermogen ook wel uitgedrukt in PK.
<span>bron: RDW</span> ">
        Vermogen
    <span data-toggle="tooltip" data-html="true" title="<strong>Vermogen</strong><br/>Dit is de energie die een motor kan leveren om een voertuig in beweging te brengen, uitgedrukt in kW. De RDW registreert dit voor personenauto's, bedrijfsauto's, driewielige motorvoertuigen, motorfietsen en bromfietsen. Vroeger werd het vermogen ook wel uitgedrukt in PK.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Vermogen</strong><br/>Dit is de energie die een motor kan leveren om een voertuig in beweging te brengen, uitgedrukt in kW. De RDW registreert dit voor personenauto's, bedrijfsauto's, driewielige motorvoertuigen, motorfietsen en bromfietsen. Vroeger werd het vermogen ook wel uitgedrukt in PK.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
125 kW (170 PK)

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Continu (elektrisch) vermogen
    </div>
    <div class="col-6 col-sm-7 value">
75 kW (102 PK)

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Max. continu (elektrisch) vermogen
    </div>
    <div class="col-6 col-sm-7 value">
75 kW (102 PK)

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Netto max. (elektrisch) vermogen
    </div>
    <div class="col-6 col-sm-7 value">
125 kW (170 PK)

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>G3</strong><br/>Een G3-gasinstallatie is een 'milieuvriendelijke' LPG-installatie, de zogenoemde derde generatie gasinstallatie. Heeft een voertuig een gasinstallatie, dan is onder de rubriek 'Gasinstallatie' op het kentekenbewijs vermeld welk soort. De RDW geeft dit aan met codes. Voor een normale gasinstallatie is dit de letter 'G' en voor een milieuvriendelijke gasinstallatie staat er 'G3' vermeld.
<span>bron: RDW</span> " title="Een G3-gasinstallatie is een 'milieuvriendelijke' LPG-installatie, de zogenoemde derde generatie gasinstallatie. Heeft een voertuig een gasinstallatie, dan is onder de rubriek 'Gasinstallatie' op het kentekenbewijs vermeld welk soort. De RDW geeft dit aan met codes. Voor een normale gasinstallatie is dit de letter 'G' en voor een milieuvriendelijke gasinstallatie staat er 'G3' vermeld.
            
            
bron: RDW">G3<span data-toggle="tooltip" data-html="true" title="<strong>G3</strong><br/>Een G3-gasinstallatie is een 'milieuvriendelijke' LPG-installatie, de zogenoemde derde generatie gasinstallatie. Heeft een voertuig een gasinstallatie, dan is onder de rubriek 'Gasinstallatie' op het kentekenbewijs vermeld welk soort. De RDW geeft dit aan met codes. Voor een normale gasinstallatie is dit de letter 'G' en voor een milieuvriendelijke gasinstallatie staat er 'G3' vermeld.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>G3</strong><br/>Een G3-gasinstallatie is een 'milieuvriendelijke' LPG-installatie, de zogenoemde derde generatie gasinstallatie. Heeft een voertuig een gasinstallatie, dan is onder de rubriek 'Gasinstallatie' op het kentekenbewijs vermeld welk soort. De RDW geeft dit aan met codes. Voor een normale gasinstallatie is dit de letter 'G' en voor een milieuvriendelijke gasinstallatie staat er 'G3' vermeld.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">Nee</div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label">
        Aandrijving
    </div>
    <div class="col-6 col-sm-7 value">
Achter

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Wielbasis</strong><br/>De totale wielbasis van een voertuig in centimeters.
<span>bron: RDW</span> ">
        Wielbasis
    <span data-toggle="tooltip" data-html="true" title="<strong>Wielbasis</strong><br/>De totale wielbasis van een voertuig in centimeters.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Wielbasis</strong><br/>De totale wielbasis van een voertuig in centimeters.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
257 cm

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Koppel
    </div>
    <div class="col-6 col-sm-7 value">
250 Nm

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Tankinhoud
    </div>
    <div class="col-6 col-sm-7 value">
Niet van toepassing

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Maximaal toerental
    </div>
    <div class="col-6 col-sm-7 value">
4.800 rpm

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Max. koppel bij aant. toeren
    </div>
    <div class="col-6 col-sm-7 value">
4.800 rpm

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" title="">Turbo / Compressor</div>
    <div class="col-6 col-sm-7 value">Nee</div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label">
        Acceleratie 0-100
    </div>
    <div class="col-6 col-sm-7 value">
7,30 seconden

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Plaats VIN-Nummer
    </div>
    <div class="col-6 col-sm-7 value">
Onbekend

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Type goedkeuringsnr.
    </div>
    <div class="col-6 col-sm-7 value">
e1*2007/46*1213*10

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Gewicht</strong><br/>Ledig gewicht
Dit is het gewicht in kilogram van het voertuig zonder passagiers en zonder lading. Dit wordt voor alle voertuigsoorten geregistreerd.
<span>bron: RDW</span> ">
        Gewicht
    <span data-toggle="tooltip" data-html="true" title="<strong>Gewicht</strong><br/>Ledig gewicht<br />Dit is het gewicht in kilogram van het voertuig zonder passagiers en zonder lading. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Gewicht</strong><br/>Ledig gewicht<br />Dit is het gewicht in kilogram van het voertuig zonder passagiers en zonder lading. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
1.245 kg

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Gewicht rijklaar</strong><br/>Deze waarde geeft aan hoe zwaar een voertuig is (in kilogram) met een voor 90 procent gevulde brandstoftank. In het geval van een personenauto of bedrijfsauto wordt bovendien ook de bestuurder meegeteld (75kg).
'Massa rijklaar' is een gegeven dat sinds juni 2004 op het kentekenbewijs vermeld wordt.
<span>bron: RDW</span> ">
        Gewicht rijklaar
    <span data-toggle="tooltip" data-html="true" title="<strong>Gewicht rijklaar</strong><br/>Deze waarde geeft aan hoe zwaar een voertuig is (in kilogram) met een voor 90 procent gevulde brandstoftank. In het geval van een personenauto of bedrijfsauto wordt bovendien ook de bestuurder meegeteld (75kg).<br />'Massa rijklaar' is een gegeven dat sinds juni 2004 op het kentekenbewijs vermeld wordt.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Gewicht rijklaar</strong><br/>Deze waarde geeft aan hoe zwaar een voertuig is (in kilogram) met een voor 90 procent gevulde brandstoftank. In het geval van een personenauto of bedrijfsauto wordt bovendien ook de bestuurder meegeteld (75kg).<br />'Massa rijklaar' is een gegeven dat sinds juni 2004 op het kentekenbewijs vermeld wordt.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
1.345 kg

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Maximaal gewicht</strong><br/>Dit is het ledig gewicht van het voertuig vermeerderd met het laadvermogen in kilogram. Dit wordt voor personenauto's, bedrijfsauto's, aanhangwagens en opleggers geregistreerd.
<span>bron: RDW</span> ">
        Maximaal gewicht
    <span data-toggle="tooltip" data-html="true" title="<strong>Maximaal gewicht</strong><br/>Dit is het ledig gewicht van het voertuig vermeerderd met het laadvermogen in kilogram. Dit wordt voor personenauto's, bedrijfsauto's, aanhangwagens en opleggers geregistreerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Maximaal gewicht</strong><br/>Dit is het ledig gewicht van het voertuig vermeerderd met het laadvermogen in kilogram. Dit wordt voor personenauto's, bedrijfsauto's, aanhangwagens en opleggers geregistreerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
1.710 kg

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Max. trekgewicht ongeremd</strong><br/>Dit is het gewicht in kilogram dat het voertuig maximaal mag trekken als de aanhangwagen geen eigen reminrichting bezit. Dit wordt alleen voor personenauto's en bedrijfsauto's geregistreerd.
<span>bron: RDW</span> ">
        Max. trekgewicht ongeremd
    <span data-toggle="tooltip" data-html="true" title="<strong>Max. trekgewicht ongeremd</strong><br/>Dit is het gewicht in kilogram dat het voertuig maximaal mag trekken als de aanhangwagen geen eigen reminrichting bezit. Dit wordt alleen voor personenauto's en bedrijfsauto's geregistreerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Max. trekgewicht ongeremd</strong><br/>Dit is het gewicht in kilogram dat het voertuig maximaal mag trekken als de aanhangwagen geen eigen reminrichting bezit. Dit wordt alleen voor personenauto's en bedrijfsauto's geregistreerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Onbekend

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Max. trekgewicht geremd</strong><br/>Dit is het gewicht in kilogram dat het voertuig maximaal mag trekken als de aanhangwagen over een eigen reminrichting beschikt. Dit wordt alleen voor personenauto's en bedrijfsauto's geregistreerd.
<span>bron: RDW</span> ">
        Max. trekgewicht geremd
    <span data-toggle="tooltip" data-html="true" title="<strong>Max. trekgewicht geremd</strong><br/>Dit is het gewicht in kilogram dat het voertuig maximaal mag trekken als de aanhangwagen over een eigen reminrichting beschikt. Dit wordt alleen voor personenauto's en bedrijfsauto's geregistreerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Max. trekgewicht geremd</strong><br/>Dit is het gewicht in kilogram dat het voertuig maximaal mag trekken als de aanhangwagen over een eigen reminrichting beschikt. Dit wordt alleen voor personenauto's en bedrijfsauto's geregistreerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Onbekend

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Lengte
    </div>
    <div class="col-6 col-sm-7 value">
4.011 mm

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Breedte
    </div>
    <div class="col-6 col-sm-7 value">
1.775 mm

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Hoogte
    </div>
    <div class="col-6 col-sm-7 value">
1.598 mm

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Aantal zitplaatsen</strong><br/>Dit is het maximaal aantal aanwezige zitplaatsen voor volwassen personen, voor gebruik tijdens het rijden. Dit aantal staat vermeld op het kentekenbewijs deel 1 of deel 1A van personenauto's, bedrijfsauto's en motorfietsen.
<span>bron: RDW</span> ">
        Aantal zitplaatsen
    <span data-toggle="tooltip" data-html="true" title="<strong>Aantal zitplaatsen</strong><br/>Dit is het maximaal aantal aanwezige zitplaatsen voor volwassen personen, voor gebruik tijdens het rijden. Dit aantal staat vermeld op het kentekenbewijs deel 1 of deel 1A van personenauto's, bedrijfsauto's en motorfietsen.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Aantal zitplaatsen</strong><br/>Dit is het maximaal aantal aanwezige zitplaatsen voor volwassen personen, voor gebruik tijdens het rijden. Dit aantal staat vermeld op het kentekenbewijs deel 1 of deel 1A van personenauto's, bedrijfsauto's en motorfietsen.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
4

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Aantal wielen
    </div>
    <div class="col-6 col-sm-7 value">
4

    </div>
</div> 

</section>            <!-- ElectricInfo  -->

<section class="result stickytitle" data-sectiontype="ElectricInfo">
    <div class="result_title">
        <h3><a id="elektrischeinformatie" data-title="Elektrische informatie"></a>Elektrische informatie

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="ElectricInfo" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
</h3>
        <p>Laadtijd, elektrisch verbruik en meer</p>
    <a href="#" class="backtotop"></a></div>

    


<div class="row list">                <div class="col-sm-12 ">
                    Ontsluit alle elektrische informatie voor deze auto:
                </div>
                <div class="col-sm-12 ">
                    Onder andere:<br>• Actieradius accu<br>• Actieradius zomer<br>• Actieradius winter<br>• Gemiddeld stroomverbruik<br>• Vermogen Elektromotor<br>• Soort Accu<br>• Laadtijd<br>• Laadsnelheid<br>• Laadvermogen<br>• Accu-capaciteit<br>• Type Oplaadkabel<br>• Snellaad-aansluiting<br>• En meer!
                </div>
</div>                <div class="row center">
                    <div class="col-12 col-sm-4">
                        
<a href="/checkout/h532dt" class="button buypremium noload" data-event="buttonPremium">Alle elektrische informatie</a>
                    </div>
                </div>


</section>            <!-- Banner  -->


<div class="row center">
    <div class="col-12 col-sm-8 col-md-5 mb-4 col-lg-5 col-xl-4">
        <a ref="nofollow" href="https://finnik.nl/goto/autooverdegrens2021" target="_blank" data-event="bannerClick">
            <img class="promo" src="https://finfabackenddevstorage.blob.core.windows.net/images/france-german-environment-banner.jpg" loading="lazy">
        </a>
        <p><a href="/checkout/h532dt">Koop een premium en krijg een jaar zonder reclame</a></p>
    </div>
</div>            <!-- History  -->

<section class="result stickytitle" data-sectiontype="History">
    <div class="result_title">
        <h3><a id="historie" data-title="Historie"></a>Historie

</h3>
        <p>APK, Eigenarenoverzicht en voertuigstatus</p>
    <a href="#" class="backtotop"></a></div>

    


<div class="timeline">

<div class="container timelineicon owners right">
    <div class="timeline__content">
        <p class="data">31-12-2019</p>
        <h3>
            Nieuwe eigenaar type:

        </h3>

            <p>Voertuig geregistreerd door een rechtspersoon.</p>

    </div>
</div></div>            <div class="result_title subheader">
                <h3>Eigenarenoverzicht</h3>
            </div> 

<div class="row">
    <div class="col-6 col-sm-5 label">Rechtspersoon</div>
    <div class="col-6 col-sm-7 value">31-12-2019 - Heden</div>
</div>            <div class="result_title subheader">
                <h3>Voertuigstatus-overzicht</h3>
            </div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Aantal eigenaren</strong><br/>Het aantal keren dat het voertuig in de afgelopen 15 jaar geregistreerd is geweest op naam van een Nederlands persoon of bedrijf.
<span>bron: RDW</span> ">
        Aantal eigenaren
    <span data-toggle="tooltip" data-html="true" title="<strong>Aantal eigenaren</strong><br/>Het aantal keren dat het voertuig in de afgelopen 15 jaar geregistreerd is geweest op naam van een Nederlands persoon of bedrijf.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Aantal eigenaren</strong><br/>Het aantal keren dat het voertuig in de afgelopen 15 jaar geregistreerd is geweest op naam van een Nederlands persoon of bedrijf.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
0 (1 incl. autobedrijf)

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>WAM-verzekerd</strong><br/>De RDW neemt geen verantwoordelijkheid voor de juistheid van dit gegeven. Deze is door derden aan de RDW geleverd.

Wat is WAM?
In de Wet Aansprakelijkheidsverzekering Motorrijtuigen (WAM) is bepaald dat een motorrijtuig verzekerd moet zijn als voor het motorrijtuig een kentekenbewijs is afgegeven. Ook een motorrijtuig dat niet wordt gebruikt, moet verzekerd zijn. Het niet verzekerd zijn is bij de WAM strafbaar gesteld.

Er is één uitzondering op deze regel. De verzekeringsplicht is niet van toepassing als uit het kentekenregister blijkt dat de geldigheid van het kentekenbewijs is geschorst. Vanaf dat moment is het staan of rijden op de openbare weg niet toegestaan.

De RDW controleert op de naleving van de verzekeringsplicht. Dit doet de RDW aan de hand van het Centraal Register WAM (CRWAM). Dit register beheert de RDW.

Een verzekering moet binnen een wettelijke termijn van 28 dagen na de datum van ingang van de dekking in het CRWAM zijn aangemeld door de verzekeraar. Als een verzekering niet binnen deze termijn wordt aangemeld, moet degene die de verzekering heeft afgesloten, contact opnemen met de verzekeraar.

• Wat betekent 'Ja'
Er staat een verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van een (vorige) verzekering nog niet is beëindigd.

• Wat betekent 'Nee'
Er staat geen verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van de verzekering nog niet is aangemeld door de verzekeraar. Alléén deze kan zorgen voor een juiste registratie van de verzekering in het CRWAM.

• Wat betekent 'NVT'
Een verzekeringsregistratie is bij het betreffende kenteken niet van toepassing of de afgesloten verzekering hoeft niet geregistreerd te worden in het CRWAM.
<span>bron: RDW</span> " title="De RDW neemt geen verantwoordelijkheid voor de juistheid van dit gegeven. Deze is door derden aan de RDW geleverd.

Wat is WAM?


In de Wet Aansprakelijkheidsverzekering Motorrijtuigen (WAM) is bepaald dat een motorrijtuig verzekerd moet zijn als voor het motorrijtuig een kentekenbewijs is afgegeven. Ook een motorrijtuig dat niet wordt gebruikt, moet verzekerd zijn. Het niet verzekerd zijn is bij de WAM strafbaar gesteld.

Er is één uitzondering op deze regel. De verzekeringsplicht is niet van toepassing als uit het kentekenregister blijkt dat de geldigheid van het kentekenbewijs is geschorst. Vanaf dat moment is het staan of rijden op de openbare weg niet toegestaan.

De RDW controleert op de naleving van de verzekeringsplicht. Dit doet de RDW aan de hand van het Centraal Register WAM (CRWAM). Dit register beheert de RDW.

Een verzekering moet binnen een wettelijke termijn van 28 dagen na de datum van ingang van de dekking in het CRWAM zijn aangemeld door de verzekeraar. Als een verzekering niet binnen deze termijn wordt aangemeld, moet degene die de verzekering heeft afgesloten, contact opnemen met de verzekeraar.

• Wat betekent 'Ja'
Er staat een verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van een (vorige) verzekering nog niet is beëindigd.

• Wat betekent 'Nee'
Er staat geen verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van de verzekering nog niet is aangemeld door de verzekeraar. Alléén deze kan zorgen voor een juiste registratie van de verzekering in het CRWAM.

• Wat betekent 'NVT'
Een verzekeringsregistratie is bij het betreffende kenteken niet van toepassing of de afgesloten verzekering hoeft niet geregistreerd te worden in het CRWAM.


bron: RDW">WAM-verzekerd<span data-toggle="tooltip" data-html="true" title="<strong>WAM-verzekerd</strong><br/>De RDW neemt geen verantwoordelijkheid voor de juistheid van dit gegeven. Deze is door derden aan de RDW geleverd.<br /><br />Wat is WAM?<br />In de Wet Aansprakelijkheidsverzekering Motorrijtuigen (WAM) is bepaald dat een motorrijtuig verzekerd moet zijn als voor het motorrijtuig een kentekenbewijs is afgegeven. Ook een motorrijtuig dat niet wordt gebruikt, moet verzekerd zijn. Het niet verzekerd zijn is bij de WAM strafbaar gesteld.<br /><br />Er is één uitzondering op deze regel. De verzekeringsplicht is niet van toepassing als uit het kentekenregister blijkt dat de geldigheid van het kentekenbewijs is geschorst. Vanaf dat moment is het staan of rijden op de openbare weg niet toegestaan.<br /><br />De RDW controleert op de naleving van de verzekeringsplicht. Dit doet de RDW aan de hand van het Centraal Register WAM (CRWAM). Dit register beheert de RDW.<br /><br />Een verzekering moet binnen een wettelijke termijn van 28 dagen na de datum van ingang van de dekking in het CRWAM zijn aangemeld door de verzekeraar. Als een verzekering niet binnen deze termijn wordt aangemeld, moet degene die de verzekering heeft afgesloten, contact opnemen met de verzekeraar.<br /><br />• Wat betekent 'Ja'<br />Er staat een verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van een (vorige) verzekering nog niet is beëindigd.<br /><br />• Wat betekent 'Nee'<br />Er staat geen verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van de verzekering nog niet is aangemeld door de verzekeraar. Alléén deze kan zorgen voor een juiste registratie van de verzekering in het CRWAM.<br /><br />• Wat betekent 'NVT'<br />Een verzekeringsregistratie is bij het betreffende kenteken niet van toepassing of de afgesloten verzekering hoeft niet geregistreerd te worden in het CRWAM.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>WAM-verzekerd</strong><br/>De RDW neemt geen verantwoordelijkheid voor de juistheid van dit gegeven. Deze is door derden aan de RDW geleverd.<br /><br />Wat is WAM?<br />In de Wet Aansprakelijkheidsverzekering Motorrijtuigen (WAM) is bepaald dat een motorrijtuig verzekerd moet zijn als voor het motorrijtuig een kentekenbewijs is afgegeven. Ook een motorrijtuig dat niet wordt gebruikt, moet verzekerd zijn. Het niet verzekerd zijn is bij de WAM strafbaar gesteld.<br /><br />Er is één uitzondering op deze regel. De verzekeringsplicht is niet van toepassing als uit het kentekenregister blijkt dat de geldigheid van het kentekenbewijs is geschorst. Vanaf dat moment is het staan of rijden op de openbare weg niet toegestaan.<br /><br />De RDW controleert op de naleving van de verzekeringsplicht. Dit doet de RDW aan de hand van het Centraal Register WAM (CRWAM). Dit register beheert de RDW.<br /><br />Een verzekering moet binnen een wettelijke termijn van 28 dagen na de datum van ingang van de dekking in het CRWAM zijn aangemeld door de verzekeraar. Als een verzekering niet binnen deze termijn wordt aangemeld, moet degene die de verzekering heeft afgesloten, contact opnemen met de verzekeraar.<br /><br />• Wat betekent 'Ja'<br />Er staat een verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van een (vorige) verzekering nog niet is beëindigd.<br /><br />• Wat betekent 'Nee'<br />Er staat geen verzekering geregistreerd in het CRWAM bij het betreffende kenteken. Het is mogelijk dat de registratie van de verzekering nog niet is aangemeld door de verzekeraar. Alléén deze kan zorgen voor een juiste registratie van de verzekering in het CRWAM.<br /><br />• Wat betekent 'NVT'<br />Een verzekeringsregistratie is bij het betreffende kenteken niet van toepassing of de afgesloten verzekering hoeft niet geregistreerd te worden in het CRWAM.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">Ja</div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Eerste toelating nationaal</strong><br/>De datum die aangeeft wanneer het betreffende kentekenbewijs voor het eerst in Nederland is tenaamgesteld. Dit wordt voor alle voertuigsoorten geregistreerd.
<span>bron: RDW</span> ">
        Eerste toelating nationaal
    <span data-toggle="tooltip" data-html="true" title="<strong>Eerste toelating nationaal</strong><br/>De datum die aangeeft wanneer het betreffende kentekenbewijs voor het eerst in Nederland is tenaamgesteld. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Eerste toelating nationaal</strong><br/>De datum die aangeeft wanneer het betreffende kentekenbewijs voor het eerst in Nederland is tenaamgesteld. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
        31-12-2019
    </div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Datum aansprakelijkheid</strong><br/>Op deze datum wordt de eigenaar of houder van het voertuig in het kentekenregister geregistreerd en daarvan wordt als bewijs een kentekenbewijs deel II, of deel IB (na 1 juni 2004) afgegeven.

Met ingang van deze datum is de geregistreerde eigenaar of houder aansprakelijk voor de wettelijke voertuigverplichtingen zoals APK, de wettelijke aansprakelijkheidsverzekering en houderschapsbelasting voor dat voertuig. Dit wordt voor alle voertuigsoorten geregistreerd.

Is deze datum niet weergegeven, dan is in het kentekenregister geen eigenaar of houder bekend met actuele aansprakelijkheid voor de wettelijke voertuigverplichtingen.
<span>bron: RDW</span> ">
        Datum aansprakelijkheid
    <span data-toggle="tooltip" data-html="true" title="<strong>Datum aansprakelijkheid</strong><br/>Op deze datum wordt de eigenaar of houder van het voertuig in het kentekenregister geregistreerd en daarvan wordt als bewijs een kentekenbewijs deel II, of deel IB (na 1 juni 2004) afgegeven.<br /><br />Met ingang van deze datum is de geregistreerde eigenaar of houder aansprakelijk voor de wettelijke voertuigverplichtingen zoals APK, de wettelijke aansprakelijkheidsverzekering en houderschapsbelasting voor dat voertuig. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><br />Is deze datum niet weergegeven, dan is in het kentekenregister geen eigenaar of houder bekend met actuele aansprakelijkheid voor de wettelijke voertuigverplichtingen.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Datum aansprakelijkheid</strong><br/>Op deze datum wordt de eigenaar of houder van het voertuig in het kentekenregister geregistreerd en daarvan wordt als bewijs een kentekenbewijs deel II, of deel IB (na 1 juni 2004) afgegeven.<br /><br />Met ingang van deze datum is de geregistreerde eigenaar of houder aansprakelijk voor de wettelijke voertuigverplichtingen zoals APK, de wettelijke aansprakelijkheidsverzekering en houderschapsbelasting voor dat voertuig. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><br />Is deze datum niet weergegeven, dan is in het kentekenregister geen eigenaar of houder bekend met actuele aansprakelijkheid voor de wettelijke voertuigverplichtingen.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
        31-12-2019
    </div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" title="">Parallel geïmporteerd</div>
    <div class="col-6 col-sm-7 value">Nee</div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Vervaldatum APK</strong><br/>Let op: de APK datum die hier getoond wordt is aangepast aan de nieuwe regels voor de periodieke keuring, die per 1 januari 2008 van kracht zijn. Op basis van deze regels is je (nieuwe) vervaldatum berekend. Meer informatie vindt je op deze site en op www.apk.nl.

De vervaldatum APK is de datum waarop de geldigheid van de APK is vervallen. De vermelde datum is de meest actuele vervaldatum APK die geregistreerd is bij de RDW en kan in het verleden liggen. Van geschorste voertuigen wordt wel de laatst bekende vervaldatum APK getoond, dit ondanks dat de APK-verplichting is opgeschort. Van voertuigen die nog nooit APK gekeurd zijn, wordt de datum gegeven vanaf wanneer de APK-plicht ingaat. Deze datum wordt berekend op basis van de datum eerste toelating. Op de datum die je te zien krijgt, moet je voertuig goedgekeurd zijn. Als er geen datum wordt gemeld, is er op dit moment geen vervaldatum APK bekend.
De RDW controleert steekproefsgewijs zo'n drie procent van de auto's die een APK-keuring ondergaan. Als het resultaat van zo'n steekproef afwijkt van het oorspronkelijke keuringsresultaat, kan het langer duren voor dit in deze database is verwerkt.
Deze vervaldatum wordt getoond voor alle voertuigsoorten met uitzondering van aanhangwagens en opleggers met een maximum massa voertuig onder de 3501 kg, driewielige motorrijtuigen onder de 400 kg, motorfietsen en bromfietsen.
<span>bron: RDW</span> ">
        Vervaldatum APK
    <span data-toggle="tooltip" data-html="true" title="<strong>Vervaldatum APK</strong><br/>Let op: de APK datum die hier getoond wordt is aangepast aan de nieuwe regels voor de periodieke keuring, die per 1 januari 2008 van kracht zijn. Op basis van deze regels is je (nieuwe) vervaldatum berekend. Meer informatie vindt je op deze site en op www.apk.nl.<br /><br />De vervaldatum APK is de datum waarop de geldigheid van de APK is vervallen. De vermelde datum is de meest actuele vervaldatum APK die geregistreerd is bij de RDW en kan in het verleden liggen. Van geschorste voertuigen wordt wel de laatst bekende vervaldatum APK getoond, dit ondanks dat de APK-verplichting is opgeschort. Van voertuigen die nog nooit APK gekeurd zijn, wordt de datum gegeven vanaf wanneer de APK-plicht ingaat. Deze datum wordt berekend op basis van de datum eerste toelating. Op de datum die je te zien krijgt, moet je voertuig goedgekeurd zijn. Als er geen datum wordt gemeld, is er op dit moment geen vervaldatum APK bekend.<br />De RDW controleert steekproefsgewijs zo'n drie procent van de auto's die een APK-keuring ondergaan. Als het resultaat van zo'n steekproef afwijkt van het oorspronkelijke keuringsresultaat, kan het langer duren voor dit in deze database is verwerkt.<br />Deze vervaldatum wordt getoond voor alle voertuigsoorten met uitzondering van aanhangwagens en opleggers met een maximum massa voertuig onder de 3501 kg, driewielige motorrijtuigen onder de 400 kg, motorfietsen en bromfietsen.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Vervaldatum APK</strong><br/>Let op: de APK datum die hier getoond wordt is aangepast aan de nieuwe regels voor de periodieke keuring, die per 1 januari 2008 van kracht zijn. Op basis van deze regels is je (nieuwe) vervaldatum berekend. Meer informatie vindt je op deze site en op www.apk.nl.<br /><br />De vervaldatum APK is de datum waarop de geldigheid van de APK is vervallen. De vermelde datum is de meest actuele vervaldatum APK die geregistreerd is bij de RDW en kan in het verleden liggen. Van geschorste voertuigen wordt wel de laatst bekende vervaldatum APK getoond, dit ondanks dat de APK-verplichting is opgeschort. Van voertuigen die nog nooit APK gekeurd zijn, wordt de datum gegeven vanaf wanneer de APK-plicht ingaat. Deze datum wordt berekend op basis van de datum eerste toelating. Op de datum die je te zien krijgt, moet je voertuig goedgekeurd zijn. Als er geen datum wordt gemeld, is er op dit moment geen vervaldatum APK bekend.<br />De RDW controleert steekproefsgewijs zo'n drie procent van de auto's die een APK-keuring ondergaan. Als het resultaat van zo'n steekproef afwijkt van het oorspronkelijke keuringsresultaat, kan het langer duren voor dit in deze database is verwerkt.<br />Deze vervaldatum wordt getoond voor alle voertuigsoorten met uitzondering van aanhangwagens en opleggers met een maximum massa voertuig onder de 3501 kg, driewielige motorrijtuigen onder de 400 kg, motorfietsen en bromfietsen.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
        31-12-2023
    </div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Status kenteken</strong><br/>• Geldig: voertuig behoort tot rijdend wagenpark.
• Ongeldig: i.v.m. vervangend kenteken of buiten normale registratie geplaatst.
• Gedemonteerd: voertuig is gedemonteerd.
• Geexporteerd: voertuig is geexporteerd.
• Onbekend: geen gegevens over bekend bij VWE.
• Wacht op keuren: Als een voertuig heel erg beschadigd is, kan de politie of de verzekeraar het kenteken de status 'wachten op keuren' (WOK) meegeven. Alleen na een keuring door de RDW wordt deze status opgeheven. Tot die tijd mag niet met het voertuig op de openbare weg gereden worden. Als je voertuig een WOK status heeft, is rijden met het betreffende voertuig een misdrijf.
<span>bron: RDW</span> ">
        Status kenteken
    <span data-toggle="tooltip" data-html="true" title="<strong>Status kenteken</strong><br/>• Geldig: voertuig behoort tot rijdend wagenpark.<br />• Ongeldig: i.v.m. vervangend kenteken of buiten normale registratie geplaatst.<br />• Gedemonteerd: voertuig is gedemonteerd.<br />• Geexporteerd: voertuig is geexporteerd.<br />• Onbekend: geen gegevens over bekend bij VWE.<br />• Wacht op keuren: Als een voertuig heel erg beschadigd is, kan de politie of de verzekeraar het kenteken de status 'wachten op keuren' (WOK) meegeven. Alleen na een keuring door de RDW wordt deze status opgeheven. Tot die tijd mag niet met het voertuig op de openbare weg gereden worden. Als je voertuig een WOK status heeft, is rijden met het betreffende voertuig een misdrijf.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Status kenteken</strong><br/>• Geldig: voertuig behoort tot rijdend wagenpark.<br />• Ongeldig: i.v.m. vervangend kenteken of buiten normale registratie geplaatst.<br />• Gedemonteerd: voertuig is gedemonteerd.<br />• Geexporteerd: voertuig is geexporteerd.<br />• Onbekend: geen gegevens over bekend bij VWE.<br />• Wacht op keuren: Als een voertuig heel erg beschadigd is, kan de politie of de verzekeraar het kenteken de status 'wachten op keuren' (WOK) meegeven. Alleen na een keuring door de RDW wordt deze status opgeheven. Tot die tijd mag niet met het voertuig op de openbare weg gereden worden. Als je voertuig een WOK status heeft, is rijden met het betreffende voertuig een misdrijf.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Geldig

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Geëxporteerd</strong><br/>Als een voertuig is geëxporteerd, zijn de gegevens hiervan nog 2 jaar te raadplegen vanaf de exportdatum. De gegevens van een geëxporteerd voertuig worden door de RDW niet meer bijgewerkt.
<span>bron: RDW</span> " title="Als een voertuig is geëxporteerd, zijn de gegevens hiervan nog 2 jaar te raadplegen vanaf de exportdatum. De gegevens van een geëxporteerd voertuig worden door de RDW niet meer bijgewerkt.


bron: RDW">Geëxporteerd<span data-toggle="tooltip" data-html="true" title="<strong>Geëxporteerd</strong><br/>Als een voertuig is geëxporteerd, zijn de gegevens hiervan nog 2 jaar te raadplegen vanaf de exportdatum. De gegevens van een geëxporteerd voertuig worden door de RDW niet meer bijgewerkt.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Geëxporteerd</strong><br/>Als een voertuig is geëxporteerd, zijn de gegevens hiervan nog 2 jaar te raadplegen vanaf de exportdatum. De gegevens van een geëxporteerd voertuig worden door de RDW niet meer bijgewerkt.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">Nee</div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" title="">Gesloopt</div>
    <div class="col-6 col-sm-7 value">Nee</div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Wacht Op Keuren (WOK)</strong><br/>De status ‘Wachten op keuring’ (WOK) wordt toegekend als een voertuig niet meer aan de permanente eisen voldoet. Dit komt voor bij lichte en zware schade aan het voertuig, maar bijvoorbeeld ook bij een uitlaat die teveel geluid maakt, bij ruitfolie die de zichtbaarheid te veel vermindert of bij opgevoerde bromfietsen. Verzekeraars, politie en RDW kunnen een WOK-status toekennen. Het voertuig mag pas weer op de openbare weg komen als het door de RDW is goedgekeurd. ">
        Wacht Op Keuren (WOK)
    <span data-toggle="tooltip" data-html="true" title="<strong>Wacht Op Keuren (WOK)</strong><br/>De status ‘Wachten op keuring’ (WOK) wordt toegekend als een voertuig niet meer aan de permanente eisen voldoet. Dit komt voor bij lichte en zware schade aan het voertuig, maar bijvoorbeeld ook bij een uitlaat die teveel geluid maakt, bij ruitfolie die de zichtbaarheid te veel vermindert of bij opgevoerde bromfietsen. Verzekeraars, politie en RDW kunnen een WOK-status toekennen. Het voertuig mag pas weer op de openbare weg komen als het door de RDW is goedgekeurd. "></span><span data-toggle="tooltip" data-html="true" title="<strong>Wacht Op Keuren (WOK)</strong><br/>De status ‘Wachten op keuring’ (WOK) wordt toegekend als een voertuig niet meer aan de permanente eisen voldoet. Dit komt voor bij lichte en zware schade aan het voertuig, maar bijvoorbeeld ook bij een uitlaat die teveel geluid maakt, bij ruitfolie die de zichtbaarheid te veel vermindert of bij opgevoerde bromfietsen. Verzekeraars, politie en RDW kunnen een WOK-status toekennen. Het voertuig mag pas weer op de openbare weg komen als het door de RDW is goedgekeurd. "></span></div>
    <div class="col-6 col-sm-7 value">
Nee

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="Wacht Op Keuren (WOK)" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" title="">Ongeldig</div>
    <div class="col-6 col-sm-7 value">Nee</div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label withbutton">
Heeft dit voertuig schade gehad?    </div>
    <div class="col-6 col-sm-5">
        
<a href="https://www.autoverleden.nl/prive/betaalMethode_volledig.php?site=www.finnik.nl&amp;kenteken=h532dt" target="_blank" class="button external" data-targethost="autoverleden.nl" data-event="buttonExternal">Check het nu!</a>
    </div>
</div>

</section>            <!-- MaintenanceAndRepairs  -->

<section class="result stickytitle" data-sectiontype="MaintenanceAndRepairs">
    <div class="result_title">
        <h3><a id="onderhoudenreparatie" data-title="Onderhoud en reparatie"></a>Onderhoud en reparatie

</h3>
        <p>APK, reparaties en terugroepacties</p>
    <a href="#" class="backtotop"></a></div>

    




<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Datum APK</strong><br/>Let op: de APK datum die hier getoond wordt is aangepast aan de nieuwe regels voor de periodieke keuring, die per 1 januari 2008 van kracht zijn. Op basis van deze regels is je (nieuwe) vervaldatum berekend. Meer informatie vindt je op deze site en op www.apk.nl.

De vervaldatum APK is de datum waarop de geldigheid van de APK is vervallen. De vermelde datum is de meest actuele vervaldatum APK die geregistreerd is bij de RDW en kan in het verleden liggen. Van geschorste voertuigen wordt wel de laatst bekende vervaldatum APK getoond, dit ondanks dat de APK-verplichting is opgeschort. Van voertuigen die nog nooit APK gekeurd zijn, wordt de datum gegeven vanaf wanneer de APK-plicht ingaat. Deze datum wordt berekend op basis van de datum eerste toelating. Op de datum die je te zien krijgt, moet je voertuig goedgekeurd zijn. Als er geen datum wordt gemeld, is er op dit moment geen vervaldatum APK bekend.
De RDW controleert steekproefsgewijs zo'n drie procent van de auto's die een APK-keuring ondergaan. Als het resultaat van zo'n steekproef afwijkt van het oorspronkelijke keuringsresultaat, kan het langer duren voor dit in deze database is verwerkt.
Deze vervaldatum wordt getoond voor alle voertuigsoorten met uitzondering van aanhangwagens en opleggers met een maximum massa voertuig onder de 3501 kg, driewielige motorrijtuigen onder de 400 kg, motorfietsen en bromfietsen.
<span>bron: RDW</span> ">
        Datum APK
    <span data-toggle="tooltip" data-html="true" title="<strong>Datum APK</strong><br/>Let op: de APK datum die hier getoond wordt is aangepast aan de nieuwe regels voor de periodieke keuring, die per 1 januari 2008 van kracht zijn. Op basis van deze regels is je (nieuwe) vervaldatum berekend. Meer informatie vindt je op deze site en op www.apk.nl.<br /><br />De vervaldatum APK is de datum waarop de geldigheid van de APK is vervallen. De vermelde datum is de meest actuele vervaldatum APK die geregistreerd is bij de RDW en kan in het verleden liggen. Van geschorste voertuigen wordt wel de laatst bekende vervaldatum APK getoond, dit ondanks dat de APK-verplichting is opgeschort. Van voertuigen die nog nooit APK gekeurd zijn, wordt de datum gegeven vanaf wanneer de APK-plicht ingaat. Deze datum wordt berekend op basis van de datum eerste toelating. Op de datum die je te zien krijgt, moet je voertuig goedgekeurd zijn. Als er geen datum wordt gemeld, is er op dit moment geen vervaldatum APK bekend.<br />De RDW controleert steekproefsgewijs zo'n drie procent van de auto's die een APK-keuring ondergaan. Als het resultaat van zo'n steekproef afwijkt van het oorspronkelijke keuringsresultaat, kan het langer duren voor dit in deze database is verwerkt.<br />Deze vervaldatum wordt getoond voor alle voertuigsoorten met uitzondering van aanhangwagens en opleggers met een maximum massa voertuig onder de 3501 kg, driewielige motorrijtuigen onder de 400 kg, motorfietsen en bromfietsen.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Datum APK</strong><br/>Let op: de APK datum die hier getoond wordt is aangepast aan de nieuwe regels voor de periodieke keuring, die per 1 januari 2008 van kracht zijn. Op basis van deze regels is je (nieuwe) vervaldatum berekend. Meer informatie vindt je op deze site en op www.apk.nl.<br /><br />De vervaldatum APK is de datum waarop de geldigheid van de APK is vervallen. De vermelde datum is de meest actuele vervaldatum APK die geregistreerd is bij de RDW en kan in het verleden liggen. Van geschorste voertuigen wordt wel de laatst bekende vervaldatum APK getoond, dit ondanks dat de APK-verplichting is opgeschort. Van voertuigen die nog nooit APK gekeurd zijn, wordt de datum gegeven vanaf wanneer de APK-plicht ingaat. Deze datum wordt berekend op basis van de datum eerste toelating. Op de datum die je te zien krijgt, moet je voertuig goedgekeurd zijn. Als er geen datum wordt gemeld, is er op dit moment geen vervaldatum APK bekend.<br />De RDW controleert steekproefsgewijs zo'n drie procent van de auto's die een APK-keuring ondergaan. Als het resultaat van zo'n steekproef afwijkt van het oorspronkelijke keuringsresultaat, kan het langer duren voor dit in deze database is verwerkt.<br />Deze vervaldatum wordt getoond voor alle voertuigsoorten met uitzondering van aanhangwagens en opleggers met een maximum massa voertuig onder de 3501 kg, driewielige motorrijtuigen onder de 400 kg, motorfietsen en bromfietsen.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
        31-12-2023
    </div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label">
        APK-bevindingen
    </div>
    <div class="col-6 col-sm-7 value">
Geen

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Onderhoudregistratie(s)
    </div>
    <div class="col-6 col-sm-7 value">
Geen

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Geregistreerde APK-reparaties voor BMW - i3
    </div>
    <div class="col-6 col-sm-7 value">
Geen

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Terugroepacties
    </div>
    <div class="col-6 col-sm-7 value">
Geen

    </div>
</div>             <div class="result_title subheader">
                <h3>Meest voorkomende reparaties</h3>
            </div> 

    <div class="row">
        <div class="col-12 label">
            Er is onvoldoende data beschikbaar van deze auto om een betrouwbaar resultaat te laten zien op de meest voorkomende reparaties.
        </div>
    </div>


</section>            <!-- AdvertSecond  -->

<div class="row center">
    <div class="col-12 col-sm-8 col-md-5 col-lg-5 col-xl-4 adsense">
        <script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4962815710377677" crossorigin="anonymous"></script>
        <!-- Finnik website ad -->
        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-4962815710377677" data-ad-slot="4985070501" data-ad-format="auto" data-adtest="off" data-full-width-responsive="true"></ins>
        <script>
            (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
    </div>
</div>            <!-- OptionsAndAccessories  -->

<section class="result stickytitle" data-sectiontype="OptionsAndAccessories">
    <div class="result_title">
        <h3><a id="optiesenaccessoires" data-title="Opties en accessoires"></a>Opties en accessoires

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="OptionsAndAccessories" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
</h3>
        <p>Niet standaard, soms handig, soms gewoon leuk</p>
    <a href="#" class="backtotop"></a></div>

    


<div class="row list">                <div class="col-sm-12 ">
                    Ontsluit de opties en accessoires voor deze auto. Bijvoorbeeld:
                </div>
                <div class="col-sm-12 ">
                    • Anti Blokkeer Systeem	 <br>• Bestuurdersairbag<br>• Centrale deurvergrendeling<br>• Elektronisch Stabiliteits Programma	<br>• Hill hold-functie 	  <br>• Multimedia-voorbereiding	 <br>• Radio/CD/MP3-speler	 <br>• Start/stop-systeem	 <br>• Alarm klasse 1(startblokkering)
                </div>
</div>                <div class="row center">
                    <div class="col-12 col-sm-4">
                        
<a href="/checkout/h532dt" class="button buypremium noload" data-event="buttonPremium">Alle opties en accessoires</a>
                    </div>
                </div>


</section>            <!-- BuyPremium  -->


<section class="premiumsection result">
    <div class="result_title">
        <h3>Krijg ontbrekende premiumgegevens over deze BMW - i3</h3>
        <p>Er zijn 6 belangrijke datapunten die je mist.</p>
    </div>
    <div class="value_items">
        <div class="row">
                        <div class="col-sm-6 col-md-4 mb-4">
                            <div class="icon wok" data-origbgimage="none">
                                <h6>Wacht Op Keuren (WOK)</h6>
                                Zoek uit of dit voertuig voldoet aan de wettelijke eisen of dat het nog moet wachten op een keuring.
                            </div>
                        </div>                        <div class="col-sm-6 col-md-4 mb-4">
                            <div class="icon netherlands" data-origbgimage="url(&quot;https://finnik.nl/svg/netherlands/fff.svg&quot;)">
                                <h6>Elektrische informatie</h6>
                                Alle elektrische informatie over deze auto. Zie de actieradius, verbruik, vermogen, laadtijd, laadsnelheid en veel meer!
                            </div>
                        </div>                        <div class="col-sm-6 col-md-4 mb-4">
                            <div class="icon legoblock" data-origbgimage="url(&quot;https://finnik.nl/svg/legoblock/fff.svg&quot;)">
                                <h6>Opties en accessoires</h6>
                                Alle opties en accessoires die van toepassing zijn op de auto. Geen reden om te gissen met een Premium Kentekecheck.
                            </div>
                        </div>                        <div class="col-sm-6 col-md-4 mb-4">
                            <div class="icon euro" data-origbgimage="url(&quot;https://finnik.nl/svg/euro/fff.svg&quot;)">
                                <h6>Total Cost of Ownership</h6>
                                Geeft inzicht in de kosten voor het onderhoud, afschrijving, brandstof, banden en wegenbelasting op voertuigniveau.
                            </div>
                        </div>                        <div class="col-sm-6 col-md-4 mb-4">
                            <div class="icon euro" data-origbgimage="url(&quot;https://finnik.nl/svg/euro/fff.svg&quot;)">
                                <h6>Exacte waarde</h6>
                                Met de exacte waarde van de auto, weet je precies waar je aan toe bent. Of je nou een auto koopt of verkoopt.
                            </div>
                        </div>                        <div class="col-sm-6 col-md-4 mb-4">
                            <div class="icon warning" data-origbgimage="url(&quot;https://finnik.nl/svg/warning/fff.svg&quot;)">
                                <h6>Diefstalcheck</h6>
                                Zie hoeveel van deze auto's het afgelopen jaar zijn gestolen en wat onze voorspelling is voor het komende jaar. Plus meer!
                            </div>
                        </div>                        <div class="col-12 col-sm-12">
                            <div class="row center">
                                <div class="col-12 col-sm-4">
                                    
<a href="/checkout/h532dt" class="button buypremium noload" data-event="buttonPremium">Premium voor € 3,99</a>
                                </div>
                            </div>
                        </div>
        </div>
    </div>
</section>            <!-- TotalCostOfOwnership  -->

<section class="result stickytitle" data-sectiontype="TotalCostOfOwnership">
    <div class="result_title">
        <h3><a id="totalekostenpermaand" data-title="Totale kosten per maand"></a>Totale kosten per maand

</h3>
        <p>Hoeveel kost deze BMW in gebruik?</p>
    <a href="#" class="backtotop"></a></div>

    


<div class="row list">                <div class="col-sm-12 ">
                    Vraag de volgende gepersonaliseerde kosten aan en krijg een gedetailleerde kosten overzicht voor:
                </div>
                <div class="col-sm-12 ">
                    • Onderhoudskosten<br>• Afschrijvingskosten<br>• Brandstofkosten<br>• Bandenkosten<br>• Verzekeringskosten<br>• Kosten wegenbelasting<br>• Totale maandelijkse kosten
                </div>
</div>                <div class="row center">
                    <div class="col-12 col-sm-4">
                        
<a href="/checkout/h532dt" class="button buypremium noload" data-event="buttonPremium">Totale kosten per maand</a>
                    </div>
                </div>


</section>            <!-- ValueInformation  -->

<section class="result stickytitle" data-sectiontype="ValueInformation">
    <div class="result_title">
        <h3><a id="waarde-informatie" data-title="Waarde-informatie"></a>Waarde-informatie

</h3>
        <p>Exacte waarde, belasting en bijtelling</p>
    <a href="#" class="backtotop"></a></div>

    




<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Nieuwprijs</strong><br/>De door de officiële importeur in Nederland gepubliceerde prijs.
Wat je hier ziet is de catalogusprijs inclusief de BPM en BTW, ook wel ‘fiscale waarde’ genoemd. 
Je kunt deze waarde gebruiken voor berekening van de ‘bijtelling privé gebruik auto’ in je belastingaangifte.
<span>bron: RDW</span> ">
        Nieuwprijs
    <span data-toggle="tooltip" data-html="true" title="<strong>Nieuwprijs</strong><br/>De door de officiële importeur in Nederland gepubliceerde prijs.<br />Wat je hier ziet is de catalogusprijs inclusief de BPM en BTW, ook wel ‘fiscale waarde’ genoemd. <br />Je kunt deze waarde gebruiken voor berekening van de ‘bijtelling privé gebruik auto’ in je belastingaangifte.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="" data-original-title="<strong>Nieuwprijs</strong><br/>De door de officiële importeur in Nederland gepubliceerde prijs.<br />Wat je hier ziet is de catalogusprijs inclusief de BPM en BTW, ook wel ‘fiscale waarde’ genoemd. <br />Je kunt deze waarde gebruiken voor berekening van de ‘bijtelling privé gebruik auto’ in je belastingaangifte.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
€ 46.660,-

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Waarde-indicatie</strong><br/>De hier getoonde waarde geeft een indicatie van de Exacte waarde ofwel dagwaarde. De dagwaarde van een auto is de waarde die de auto op dit moment waard is. De dagwaarde is ook de waarde die je terug krijgt van de verzekering als je auto total loss wordt verklaard. De dagwaarde kan ook worden gezien als de vervangingswaarde. De waarde waarvoor je op dat moment een vergelijkbare auto zou kunnen kopen.
<span>Bron: VWE</span> ">
        Waarde-indicatie
    <span data-toggle="tooltip" data-html="true" title="<strong>Waarde-indicatie</strong><br/>De hier getoonde waarde geeft een indicatie van de Exacte waarde ofwel dagwaarde. De dagwaarde van een auto is de waarde die de auto op dit moment waard is. De dagwaarde is ook de waarde die je terug krijgt van de verzekering als je auto total loss wordt verklaard. De dagwaarde kan ook worden gezien als de vervangingswaarde. De waarde waarvoor je op dat moment een vergelijkbare auto zou kunnen kopen.<br /><span>Bron: VWE</span> "></span><span data-toggle="tooltip" data-html="true" title="" data-original-title="<strong>Waarde-indicatie</strong><br/>De hier getoonde waarde geeft een indicatie van de Exacte waarde ofwel dagwaarde. De dagwaarde van een auto is de waarde die de auto op dit moment waard is. De dagwaarde is ook de waarde die je terug krijgt van de verzekering als je auto total loss wordt verklaard. De dagwaarde kan ook worden gezien als de vervangingswaarde. De waarde waarvoor je op dat moment een vergelijkbare auto zou kunnen kopen.<br /><span>Bron: VWE</span> "></span></div>
    <div class="col-6 col-sm-7 value">
€ 27-32k

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Exacte waarde</strong><br/>De dagwaarde van een auto is de waarde die de auto op dit moment waard is. 
De dagwaarde is ook de waarde die je terug krijgt van de verzekering als je auto total loss wordt verklaard. De dagwaarde kan ook worden gezien als de vervangingswaarde. De waarde waarvoor je op dat moment een vergelijkbare auto zou kunnen kopen.
<span>Bron: VWE</span> ">
        Exacte waarde
    <span data-toggle="tooltip" data-html="true" title="<strong>Exacte waarde</strong><br/>De dagwaarde van een auto is de waarde die de auto op dit moment waard is. <br />De dagwaarde is ook de waarde die je terug krijgt van de verzekering als je auto total loss wordt verklaard. De dagwaarde kan ook worden gezien als de vervangingswaarde. De waarde waarvoor je op dat moment een vergelijkbare auto zou kunnen kopen.<br /><span>Bron: VWE</span> "></span><span data-toggle="tooltip" data-html="true" title="" data-original-title="<strong>Exacte waarde</strong><br/>De dagwaarde van een auto is de waarde die de auto op dit moment waard is. <br />De dagwaarde is ook de waarde die je terug krijgt van de verzekering als je auto total loss wordt verklaard. De dagwaarde kan ook worden gezien als de vervangingswaarde. De waarde waarvoor je op dat moment een vergelijkbare auto zou kunnen kopen.<br /><span>Bron: VWE</span> "></span></div>
    <div class="col-6 col-sm-7 value">
••••••

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="Exacte waarde" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Inruilwaarde</strong><br/>De inruilwaarde is de waarde die een autobedrijf geeft voor je auto als je hem daar wilt inruilen. 
Als je een nieuwe auto bij hetzelfde autobedrijf koopt wordt de inruilwaarde van je auto vaak meegenomen in de onderhandeling over de prijs van je nieuwe auto. De inruilwaarde wordt online meestal berekend op basis van merk, model, leeftijd en kilometerstand. Bij de dagwaarde worden veelal ook de opties en accessoires meegenomen in de prijsberekening.
<span>Bron: VWE</span> ">
        Inruilwaarde
    <span data-toggle="tooltip" data-html="true" title="<strong>Inruilwaarde</strong><br/>De inruilwaarde is de waarde die een autobedrijf geeft voor je auto als je hem daar wilt inruilen. <br />Als je een nieuwe auto bij hetzelfde autobedrijf koopt wordt de inruilwaarde van je auto vaak meegenomen in de onderhandeling over de prijs van je nieuwe auto. De inruilwaarde wordt online meestal berekend op basis van merk, model, leeftijd en kilometerstand. Bij de dagwaarde worden veelal ook de opties en accessoires meegenomen in de prijsberekening.<br /><span>Bron: VWE</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Inruilwaarde</strong><br/>De inruilwaarde is de waarde die een autobedrijf geeft voor je auto als je hem daar wilt inruilen. <br />Als je een nieuwe auto bij hetzelfde autobedrijf koopt wordt de inruilwaarde van je auto vaak meegenomen in de onderhandeling over de prijs van je nieuwe auto. De inruilwaarde wordt online meestal berekend op basis van merk, model, leeftijd en kilometerstand. Bij de dagwaarde worden veelal ook de opties en accessoires meegenomen in de prijsberekening.<br /><span>Bron: VWE</span> "></span></div>
    <div class="col-6 col-sm-7 value">
••••••

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="Inruilwaarde" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>BPM</strong><br/>BPM staat voor Belasting Personenauto's en Motorrijwielen. BPM is een belasting die eenmalig moet worden betaald door degene die als eerste een personenauto, bestelauto of motorrijwiel op zijn naam laat registreren.

Koop je in Nederland een nieuwe personenauto, bestelauto of een nieuw motorrijwiel, dan verzorgt de importeur de aangifte en de betaling van de BPM voor je. Het bruto betaalde BPM-bedrag staat bij deze nieuw gekochte voertuigen vermeld op het kentekenbewijs (deel 1A).

Voor het verkrijgen van een Nederlands kenteken, moet je in de volgende situaties zelf aangifte doen van BPM:
• Als je een personenauto, bestelauto of een motorrijwiel uit het buitenland haalt
• Als je een bestelauto die vóór 1 juli 2005 in gebruik is genomen, ombouwt tot personenauto.

Achter het onderwerp BPM leest u het bruto bedrag in euro's.
Als je de melding n.v.t. terugkrijgt, betekent dat, dat op het moment van eerste afgifte van het kentekenbewijs geen BPM verschuldigd was.
<span>bron: RDW</span> ">
        BPM
    <span data-toggle="tooltip" data-html="true" title="<strong>BPM</strong><br/>BPM staat voor Belasting Personenauto's en Motorrijwielen. BPM is een belasting die eenmalig moet worden betaald door degene die als eerste een personenauto, bestelauto of motorrijwiel op zijn naam laat registreren.<br /><br />Koop je in Nederland een nieuwe personenauto, bestelauto of een nieuw motorrijwiel, dan verzorgt de importeur de aangifte en de betaling van de BPM voor je. Het bruto betaalde BPM-bedrag staat bij deze nieuw gekochte voertuigen vermeld op het kentekenbewijs (deel 1A).<br /><br />Voor het verkrijgen van een Nederlands kenteken, moet je in de volgende situaties zelf aangifte doen van BPM:<br />• Als je een personenauto, bestelauto of een motorrijwiel uit het buitenland haalt<br />• Als je een bestelauto die vóór 1 juli 2005 in gebruik is genomen, ombouwt tot personenauto.<br /><br />Achter het onderwerp BPM leest u het bruto bedrag in euro's.<br />Als je de melding n.v.t. terugkrijgt, betekent dat, dat op het moment van eerste afgifte van het kentekenbewijs geen BPM verschuldigd was.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="" data-original-title="<strong>BPM</strong><br/>BPM staat voor Belasting Personenauto's en Motorrijwielen. BPM is een belasting die eenmalig moet worden betaald door degene die als eerste een personenauto, bestelauto of motorrijwiel op zijn naam laat registreren.<br /><br />Koop je in Nederland een nieuwe personenauto, bestelauto of een nieuw motorrijwiel, dan verzorgt de importeur de aangifte en de betaling van de BPM voor je. Het bruto betaalde BPM-bedrag staat bij deze nieuw gekochte voertuigen vermeld op het kentekenbewijs (deel 1A).<br /><br />Voor het verkrijgen van een Nederlands kenteken, moet je in de volgende situaties zelf aangifte doen van BPM:<br />• Als je een personenauto, bestelauto of een motorrijwiel uit het buitenland haalt<br />• Als je een bestelauto die vóór 1 juli 2005 in gebruik is genomen, ombouwt tot personenauto.<br /><br />Achter het onderwerp BPM leest u het bruto bedrag in euro's.<br />Als je de melding n.v.t. terugkrijgt, betekent dat, dat op het moment van eerste afgifte van het kentekenbewijs geen BPM verschuldigd was.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">

12.3456

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Rest BPM
    </div>
    <div class="col-6 col-sm-7 value">
€ 0,-

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Bijtellingsklasse
    </div>
    <div class="col-6 col-sm-7 value">
4%

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Netto bijtelling
    </div>
    <div class="col-6 col-sm-7 value">
        <ul class="textlist">
                <li>37,35%: € 58,09</li>
                <li>49,50%: € 76,99</li>
        </ul>
    </div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label">
        Wegenbelasting per kwartaal
    </div>
    <div class="col-6 col-sm-7 value">
        <ul class="textlist">
                <li>Drenthe: € 0,-</li>
                <li>Flevoland: € 0,-</li>
                <li>Friesland: € 0,-</li>
                <li>Gelderland: € 0,-</li>
                <li>Groningen: € 0,-</li>
                <li>Limburg: € 0,-</li>
                <li>N-Brabant: € 0,-</li>
                <li>N-Holland: € 0,-</li>
                <li>Overijssel: € 0,-</li>
                <li>Utrecht: € 0,-</li>
                <li>Z-Holland: € 0,-</li>
                <li>Zeeland: € 0,-</li>
        </ul>
    </div>
</div>

</section>            <!-- BasicInformation  -->

<section class="result stickytitle" data-sectiontype="BasicInformation">
    <div class="result_title">
        <h3><a id="basisgegevens" data-title="Basisgegevens"></a>Basisgegevens

</h3>
        <p>Merk, model, kleur en meer</p>
    <a href="#" class="backtotop"></a></div>

    




<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Merk</strong><br/>Het merk van het voertuig. Dit wordt voor alle voertuigsoorten geregistreerd.
<span>bron: RDW</span> ">
        Merk
    <span data-toggle="tooltip" data-html="true" title="<strong>Merk</strong><br/>Het merk van het voertuig. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="" data-original-title="<strong>Merk</strong><br/>Het merk van het voertuig. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
BMW

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Model</strong><br/>Handelsbenaming van het voertuig zoals de fabrikant heeft opgegeven.

De handelsbenaming kan afwijken van de aanduiding die op het voertuig te vinden is.
<span>bron: RDW</span> ">
        Model
    <span data-toggle="tooltip" data-html="true" title="<strong>Model</strong><br/>Handelsbenaming van het voertuig zoals de fabrikant heeft opgegeven.<br /><br />De handelsbenaming kan afwijken van de aanduiding die op het voertuig te vinden is.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Model</strong><br/>Handelsbenaming van het voertuig zoals de fabrikant heeft opgegeven.<br /><br />De handelsbenaming kan afwijken van de aanduiding die op het voertuig te vinden is.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
i3

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Uitvoering</strong><br/>Model van het voertuig. Na 1995 is type op het kentekenbewijs vervangen door 'handelsbenaming'. Dit wordt voor alle voertuigsoorten geregistreerd.
<span>bron: RDW</span> ">
        Uitvoering
    <span data-toggle="tooltip" data-html="true" title="<strong>Uitvoering</strong><br/>Model van het voertuig. Na 1995 is type op het kentekenbewijs vervangen door 'handelsbenaming'. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="" data-original-title="<strong>Uitvoering</strong><br/>Model van het voertuig. Na 1995 is type op het kentekenbewijs vervangen door 'handelsbenaming'. Dit wordt voor alle voertuigsoorten geregistreerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Executive Edition 120Ah 42 kWh

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Bouwjaar
    </div>
    <div class="col-6 col-sm-7 value">
2019

    </div>
</div> 
<div class="row">
    <div class="col-6 col-sm-5 label">
        Tellerstandcontrole
    </div>
    <div class="col-6 col-sm-7 col-md-4 value">
        <a href="/KmCheck/h532dt" class="button" data-event="product:kilometer">€ 0,99</a>
    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Brandstof</strong><br/>Dit is de aanduiding van de brandstofsoort van het op het kentekenbewijs genoemde voertuig.
De RDW kent 8 brandstofsoorten, te weten:
• Benzine
• Cryogeen (gas onder hoge druk bij lage temperatuur)
• Diesel
• Electriciteit
• LPG (Liquified Petroleum Gas)
• CNG (Compressed Natural Gas, aardgas)
• Waterstof
• Alcohol
Op het kentekenbewijs tref je de brandstofcode aan. Dit is de eerste letter van de brandstof met uitzondering van G voor LPG en H voor CNG. Er kunnen maximaal twee brandstofsoorten worden geregistreerd. Voor aanhangwagens en opleggers wordt geen brandstofsoort genoteerd.
<span>bron: RDW</span> ">
        Brandstof
    <span data-toggle="tooltip" data-html="true" title="<strong>Brandstof</strong><br/>Dit is de aanduiding van de brandstofsoort van het op het kentekenbewijs genoemde voertuig.<br />De RDW kent 8 brandstofsoorten, te weten:<br />• Benzine<br />• Cryogeen (gas onder hoge druk bij lage temperatuur)<br />• Diesel<br />• Electriciteit<br />• LPG (Liquified Petroleum Gas)<br />• CNG (Compressed Natural Gas, aardgas)<br />• Waterstof<br />• Alcohol<br />Op het kentekenbewijs tref je de brandstofcode aan. Dit is de eerste letter van de brandstof met uitzondering van G voor LPG en H voor CNG. Er kunnen maximaal twee brandstofsoorten worden geregistreerd. Voor aanhangwagens en opleggers wordt geen brandstofsoort genoteerd.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Brandstof</strong><br/>Dit is de aanduiding van de brandstofsoort van het op het kentekenbewijs genoemde voertuig.<br />De RDW kent 8 brandstofsoorten, te weten:<br />• Benzine<br />• Cryogeen (gas onder hoge druk bij lage temperatuur)<br />• Diesel<br />• Electriciteit<br />• LPG (Liquified Petroleum Gas)<br />• CNG (Compressed Natural Gas, aardgas)<br />• Waterstof<br />• Alcohol<br />Op het kentekenbewijs tref je de brandstofcode aan. Dit is de eerste letter van de brandstof met uitzondering van G voor LPG en H voor CNG. Er kunnen maximaal twee brandstofsoorten worden geregistreerd. Voor aanhangwagens en opleggers wordt geen brandstofsoort genoteerd.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Elektriciteit

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Kleur</strong><br/>Kleur van het voertuig.
De RDW registreert hoofdkleuren. Lichtblauw en donkerblauw vallen bijvoorbeeld onder dezelfde kleuraanduiding, namelijk 'blauw'.
De volgende kleuren kunnen voorkomen:
• Oranje - Roze - Rood - Wit - Blauw - Groen - Geel - Grijs - Bruin - Crème - Paars - Zwart - Diversen
Alleen van personenauto's wordt de kleur geregistreerd, maximaal twee kleuren per auto.
<span>bron: RDW</span> ">
        Kleur
    <span data-toggle="tooltip" data-html="true" title="<strong>Kleur</strong><br/>Kleur van het voertuig.<br />De RDW registreert hoofdkleuren. Lichtblauw en donkerblauw vallen bijvoorbeeld onder dezelfde kleuraanduiding, namelijk 'blauw'.<br />De volgende kleuren kunnen voorkomen:<br />• Oranje - Roze - Rood - Wit - Blauw - Groen - Geel - Grijs - Bruin - Crème - Paars - Zwart - Diversen<br />Alleen van personenauto's wordt de kleur geregistreerd, maximaal twee kleuren per auto.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Kleur</strong><br/>Kleur van het voertuig.<br />De RDW registreert hoofdkleuren. Lichtblauw en donkerblauw vallen bijvoorbeeld onder dezelfde kleuraanduiding, namelijk 'blauw'.<br />De volgende kleuren kunnen voorkomen:<br />• Oranje - Roze - Rood - Wit - Blauw - Groen - Geel - Grijs - Bruin - Crème - Paars - Zwart - Diversen<br />Alleen van personenauto's wordt de kleur geregistreerd, maximaal twee kleuren per auto.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Grijs

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Voertuigsoort</strong><br/>Omschrijving van het soort voertuig zoals dat staat geregistreerd in het kentekenregister. De RDW registreert deze omschrijving voor alle voertuigsoorten.

De volgende voertuigsoorten worden onderkend:
• Personenauto
• Bedrijfsauto
• Aanhangwagen
• Motorfiets
• Driewielig motorvoertuig (wielen symmetrisch t.o.v. de lengteas)
• Bromfiets
Eerder werden er meer (van bovenstaande soorten afgeleide) voertuigsoorten geregistreerd, zoals een oplegger, een driewielige motorcarrier en een lichte invalidenwagen.
<span>bron: RDW</span> ">
        Voertuigsoort
    <span data-toggle="tooltip" data-html="true" title="<strong>Voertuigsoort</strong><br/>Omschrijving van het soort voertuig zoals dat staat geregistreerd in het kentekenregister. De RDW registreert deze omschrijving voor alle voertuigsoorten.<br /><br />De volgende voertuigsoorten worden onderkend:<br />• Personenauto<br />• Bedrijfsauto<br />• Aanhangwagen<br />• Motorfiets<br />• Driewielig motorvoertuig (wielen symmetrisch t.o.v. de lengteas)<br />• Bromfiets<br />Eerder werden er meer (van bovenstaande soorten afgeleide) voertuigsoorten geregistreerd, zoals een oplegger, een driewielige motorcarrier en een lichte invalidenwagen.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Voertuigsoort</strong><br/>Omschrijving van het soort voertuig zoals dat staat geregistreerd in het kentekenregister. De RDW registreert deze omschrijving voor alle voertuigsoorten.<br /><br />De volgende voertuigsoorten worden onderkend:<br />• Personenauto<br />• Bedrijfsauto<br />• Aanhangwagen<br />• Motorfiets<br />• Driewielig motorvoertuig (wielen symmetrisch t.o.v. de lengteas)<br />• Bromfiets<br />Eerder werden er meer (van bovenstaande soorten afgeleide) voertuigsoorten geregistreerd, zoals een oplegger, een driewielige motorcarrier en een lichte invalidenwagen.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Personenauto

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Inrichting</strong><br/>Omschrijving van de code waarmee de uitvoeringsvorm van de inrichting van een voertuig wordt aangegeven.
<span>bron: RDW</span> ">
        Inrichting
    <span data-toggle="tooltip" data-html="true" title="<strong>Inrichting</strong><br/>Omschrijving van de code waarmee de uitvoeringsvorm van de inrichting van een voertuig wordt aangegeven.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Inrichting</strong><br/>Omschrijving van de code waarmee de uitvoeringsvorm van de inrichting van een voertuig wordt aangegeven.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Sedan

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Type voertuig</strong><br/>Europese aanduiding voor het carrosserietype van een voertuig.
Deze wordt vastgesteld tijdens de goedkeuring van een voertuig uit 1 van deze Europese voertuigcategorieën:
• M1 (personenauto’s)
• M2 en M3 (bussen)
• N1-N3 (bedrijfsauto’s)
• O1-O4 (aanhangwagens
<span>bron: RDW</span> ">
        Type voertuig
    <span data-toggle="tooltip" data-html="true" title="<strong>Type voertuig</strong><br/>Europese aanduiding voor het carrosserietype van een voertuig.<br />Deze wordt vastgesteld tijdens de goedkeuring van een voertuig uit 1 van deze Europese voertuigcategorieën:<br />• M1 (personenauto’s)<br />• M2 en M3 (bussen)<br />• N1-N3 (bedrijfsauto’s)<br />• O1-O4 (aanhangwagens<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Type voertuig</strong><br/>Europese aanduiding voor het carrosserietype van een voertuig.<br />Deze wordt vastgesteld tijdens de goedkeuring van een voertuig uit 1 van deze Europese voertuigcategorieën:<br />• M1 (personenauto’s)<br />• M2 en M3 (bussen)<br />• N1-N3 (bedrijfsauto’s)<br />• O1-O4 (aanhangwagens<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Hatchb.

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Aantal deuren
    </div>
    <div class="col-6 col-sm-7 value">
5

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Soort transmissie
    </div>
    <div class="col-6 col-sm-7 value">
Automatisch

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Aantal versnellingen
    </div>
    <div class="col-6 col-sm-7 value">
Niet geregistreerd

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Segment
    </div>
    <div class="col-6 col-sm-7 value">
B (Klein)

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        SCM alarmcertificaat
    </div>
    <div class="col-6 col-sm-7 value">
Onbekend

    </div>
</div> 

</section>            <!-- Banner  -->


<div class="row center">
    <div class="col-12 col-sm-8 col-md-5 mb-4 col-lg-5 col-xl-4">
        <a ref="nofollow" href="https://finnik.nl/goto/fairkochtbanner" target="_blank" data-event="bannerClick">
            <img class="promo" src="https://finfabackendprodstorage.blob.core.windows.net/images/finnikfairkochtbanner.png" loading="lazy">
        </a>
        <p><a href="/checkout/h532dt">Koop een premium en krijg een jaar zonder reclame</a></p>
    </div>
</div>            <!-- Environment  -->

<section class="result stickytitle" data-sectiontype="Environment">
    <div class="result_title">
        <h3><a id="milieu" data-title="Milieu"></a>Milieu

</h3>
        <p>Hoe groen is deze auto en welke milieuzones</p>
    <a href="#" class="backtotop"></a></div>

    




<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Verbruik gecombineerd</strong><br/>Het brandstofverbruik tijdens een combinatie van gestandaardiseerde stadsrit- en buitenwegcycli, uitgevoerd op een rollenbank.
Eenheid = l/100 km
<span>bron: RDW</span> ">
        Verbruik gecombineerd
    <span data-toggle="tooltip" data-html="true" title="<strong>Verbruik gecombineerd</strong><br/>Het brandstofverbruik tijdens een combinatie van gestandaardiseerde stadsrit- en buitenwegcycli, uitgevoerd op een rollenbank.<br />Eenheid = l/100 km<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Verbruik gecombineerd</strong><br/>Het brandstofverbruik tijdens een combinatie van gestandaardiseerde stadsrit- en buitenwegcycli, uitgevoerd op een rollenbank.<br />Eenheid = l/100 km<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Niet geregistreerd

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Verbruik buitenweg</strong><br/>Het brandstofverbruik tijdens een gestandaardiseerde buitenwegcyclus, uitgevoerd op een rollenbank.
Eenheid = l/100 km
<span>bron: RDW</span> ">
        Verbruik buitenweg
    <span data-toggle="tooltip" data-html="true" title="<strong>Verbruik buitenweg</strong><br/>Het brandstofverbruik tijdens een gestandaardiseerde buitenwegcyclus, uitgevoerd op een rollenbank.<br />Eenheid = l/100 km<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Verbruik buitenweg</strong><br/>Het brandstofverbruik tijdens een gestandaardiseerde buitenwegcyclus, uitgevoerd op een rollenbank.<br />Eenheid = l/100 km<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Niet geregistreerd

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Verbruik stad</strong><br/>Het brandstofverbruik tijdens een gestandaardiseerde stadsritcyclus, uitgevoerd op een rollenbank.
Eenheid = l/100 km
<span>bron: RDW</span> ">
        Verbruik stad
    <span data-toggle="tooltip" data-html="true" title="<strong>Verbruik stad</strong><br/>Het brandstofverbruik tijdens een gestandaardiseerde stadsritcyclus, uitgevoerd op een rollenbank.<br />Eenheid = l/100 km<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Verbruik stad</strong><br/>Het brandstofverbruik tijdens een gestandaardiseerde stadsritcyclus, uitgevoerd op een rollenbank.<br />Eenheid = l/100 km<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Niet geregistreerd

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Elektrisch verbruik combinatierit
    </div>
    <div class="col-6 col-sm-7 value">
131 wh/km

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Elektrisch verbruik gecombineerd
    </div>
    <div class="col-6 col-sm-7 value">
131 wh/km

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Actieradius elektrisch combinatierit
    </div>
    <div class="col-6 col-sm-7 value">
359 km

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Actieradius elektrisch stad WLTP
    </div>
    <div class="col-6 col-sm-7 value">
411 km

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Actieradius elektrisch WLTP
    </div>
    <div class="col-6 col-sm-7 value">
296 km

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>CO2-Uitstoot</strong><br/>De uitstoot van CO2 tijdens een combinatie van een stads- en een buitenrit volgens bepaalde standaarden.
<span>bron: RDW</span> ">
        CO2-Uitstoot
    <span data-toggle="tooltip" data-html="true" title="<strong>CO2-Uitstoot</strong><br/>De uitstoot van CO2 tijdens een combinatie van een stads- en een buitenrit volgens bepaalde standaarden.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>CO2-Uitstoot</strong><br/>De uitstoot van CO2 tijdens een combinatie van een stads- en een buitenrit volgens bepaalde standaarden.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Niet geregistreerd

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Emissieklasse</strong><br/>Klasse van uitstoot van verontreinigende gassen en (fijnstof)deeltjes door een voertuig. Dit gegeven wordt gebruikt in het kader van milieuzones.
<span>Bron: RDW</span> ">
        Emissieklasse
    <span data-toggle="tooltip" data-html="true" title="<strong>Emissieklasse</strong><br/>Klasse van uitstoot van verontreinigende gassen en (fijnstof)deeltjes door een voertuig. Dit gegeven wordt gebruikt in het kader van milieuzones.<br /><span>Bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Emissieklasse</strong><br/>Klasse van uitstoot van verontreinigende gassen en (fijnstof)deeltjes door een voertuig. Dit gegeven wordt gebruikt in het kader van milieuzones.<br /><span>Bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Z

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Energielabel</strong><br/>Het zuinigheidslabel geeft aan hoe zuinig of onzuinig een auto is ten opzichte van andere auto's die net zo groot zijn. Hiermee kun je snel het verbruik van ongeveer even grote auto's met elkaar vergelijken. De labels worden aangegeven met de letters A tot en met G. De letter A geeft aan dat het voertuig meer dan 20 procent zuiniger is dan gemiddeld, de letter G houdt in dat het voertuig meer dan 30 procent minder zuinig is dan gemiddeld.
Het zuinigheidslabel, dat je ook op nieuwe auto's aantreft in de showroom bij autodealers, is alleen van toepassing op personenauto's met een Europese typegoedkeuring en met de primaire brandstof benzine of diesel. Het zuinigheidslabel dat je te zien krijgt, is de categorie die voor het voertuig van toepassing was op het moment van de datum van eerste tenaamstelling van het kentekenbewijs.
<span>bron: RDW</span> ">Energielabel<span data-toggle="tooltip" data-html="true" title="<strong>Energielabel</strong><br/>Het zuinigheidslabel geeft aan hoe zuinig of onzuinig een auto is ten opzichte van andere auto's die net zo groot zijn. Hiermee kun je snel het verbruik van ongeveer even grote auto's met elkaar vergelijken. De labels worden aangegeven met de letters A tot en met G. De letter A geeft aan dat het voertuig meer dan 20 procent zuiniger is dan gemiddeld, de letter G houdt in dat het voertuig meer dan 30 procent minder zuinig is dan gemiddeld.<br />Het zuinigheidslabel, dat je ook op nieuwe auto's aantreft in de showroom bij autodealers, is alleen van toepassing op personenauto's met een Europese typegoedkeuring en met de primaire brandstof benzine of diesel. Het zuinigheidslabel dat je te zien krijgt, is de categorie die voor het voertuig van toepassing was op het moment van de datum van eerste tenaamstelling van het kentekenbewijs.<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Energielabel</strong><br/>Het zuinigheidslabel geeft aan hoe zuinig of onzuinig een auto is ten opzichte van andere auto's die net zo groot zijn. Hiermee kun je snel het verbruik van ongeveer even grote auto's met elkaar vergelijken. De labels worden aangegeven met de letters A tot en met G. De letter A geeft aan dat het voertuig meer dan 20 procent zuiniger is dan gemiddeld, de letter G houdt in dat het voertuig meer dan 30 procent minder zuinig is dan gemiddeld.<br />Het zuinigheidslabel, dat je ook op nieuwe auto's aantreft in de showroom bij autodealers, is alleen van toepassing op personenauto's met een Europese typegoedkeuring en met de primaire brandstof benzine of diesel. Het zuinigheidslabel dat je te zien krijgt, is de categorie die voor het voertuig van toepassing was op het moment van de datum van eerste tenaamstelling van het kentekenbewijs.<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7"><div class="energieLabel" style="background: rgb(87, 160, 94);">A<div class="energieLabelpunt" style="background: rgb(87, 160, 94);"></div></div></div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Euroklasse</strong><br/>Voor bedrijfsvoertuigen die zwaarder zijn dan 3500 kg registreert VWE een zogenoemde Euroklasse. De Euroklasse geeft aan in hoeverre het voertuig voldoet aan de in de Europese richtlijnen vermelde minimum waarden voor de uitstoot van vervuilende stoffen.
De nu vastgestelde Euroklassen kennen de waarden 0, 1, 2, 3, 4 en 5. De waarde 0 betekent dat het voertuig veel vervuilende stoffen uitstoot en de waarde 5 betekent dat het voertuig heel weinig vervuilende stoffen uitstoot. In een aantal gevallen is geen waarde bekend of kan VWE deze niet vaststellen. Dat is bijvoorbeeld het geval bij sommige ingevoerde voertuigen.
<span>bron: VWE</span> ">
        Euroklasse
    <span data-toggle="tooltip" data-html="true" title="<strong>Euroklasse</strong><br/>Voor bedrijfsvoertuigen die zwaarder zijn dan 3500 kg registreert VWE een zogenoemde Euroklasse. De Euroklasse geeft aan in hoeverre het voertuig voldoet aan de in de Europese richtlijnen vermelde minimum waarden voor de uitstoot van vervuilende stoffen.<br />De nu vastgestelde Euroklassen kennen de waarden 0, 1, 2, 3, 4 en 5. De waarde 0 betekent dat het voertuig veel vervuilende stoffen uitstoot en de waarde 5 betekent dat het voertuig heel weinig vervuilende stoffen uitstoot. In een aantal gevallen is geen waarde bekend of kan VWE deze niet vaststellen. Dat is bijvoorbeeld het geval bij sommige ingevoerde voertuigen.<br /><span>bron: VWE</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Euroklasse</strong><br/>Voor bedrijfsvoertuigen die zwaarder zijn dan 3500 kg registreert VWE een zogenoemde Euroklasse. De Euroklasse geeft aan in hoeverre het voertuig voldoet aan de in de Europese richtlijnen vermelde minimum waarden voor de uitstoot van vervuilende stoffen.<br />De nu vastgestelde Euroklassen kennen de waarden 0, 1, 2, 3, 4 en 5. De waarde 0 betekent dat het voertuig veel vervuilende stoffen uitstoot en de waarde 5 betekent dat het voertuig heel weinig vervuilende stoffen uitstoot. In een aantal gevallen is geen waarde bekend of kan VWE deze niet vaststellen. Dat is bijvoorbeeld het geval bij sommige ingevoerde voertuigen.<br /><span>bron: VWE</span> "></span></div>
    <div class="col-6 col-sm-7 value">
Z

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Roetfilter</strong><br/>Een roetfilter is een technische voorziening in een auto die een groot deel van de roetdeeltjes opvangt die dieselmotoren uitstoten. Die roetdeeltjes vervuilen de lucht en zijn schadelijk voor de gezondheid. Inbouwen van roetfilters levert dus een bijdrage aan de verbetering van de luchtkwaliteit.
Een roetfilter kan bij personen- of bedrijfsauto's met een dieselmotor al tijdens het fabricageproces (ook wel 'affabriek' genoemd) van de auto worden ingebouwd. Met de modernste motortechnieken is het echter ook mogelijk om de roetuitstoot zonder roetfilter sterk te verminderen. Hoewel deze voertuigen hierbij niet daadwerkelijk voorzien worden van een roetfilter, registreert de RDW voor deze voertuigen wel een roetfilter, mits de roetuitstoot niet hoger is dan 0,005 gram/km.
Er zijn ook voertuigen die wel een affabriek roetfilter hebben, maar daarmee toch nog meer dan 0,005 gram/km roetdeeltjes uitstoten. De RDW registreert voor deze voertuigen dan geen Affabriek roetfilter, maar 'Nee'.
Een roetfilter kan ook achteraf (ook wel 'retrofit' genoemd) worden aangebracht in het uitlaatsysteem. Deze voertuigen krijgen de classificatie 'Retrofit'. De RDW registreert deze classificatie sinds medio 2006.
Je kunt achter het onderwerp roetfilter dus de volgende meldingen te zien krijgen:
• Ja Affabriek (bij dieselvoertuigen die affabriek niet meer roetdeeltjes uitstoten dan 0,005 gram/km)
• Ja Retrofit (bij dieselvoertuigen die achteraf (na kentekening) een roetfilter hebben gekregen)
• Nee (bij dieselvoertuigen zonder roetfilter of bij dieselvoertuigen met roetfilter die meer dan 0,005 gram/km roetdeeltjes uitstoten)
• N.v.t. (bij voertuigen die geen diesel als brandstof hebben of bij voertuigen waarvan de RDW (nog) geen roetfilters registreert)
<span>bron: RDW</span> ">
        Roetfilter
    <span data-toggle="tooltip" data-html="true" title="<strong>Roetfilter</strong><br/>Een roetfilter is een technische voorziening in een auto die een groot deel van de roetdeeltjes opvangt die dieselmotoren uitstoten. Die roetdeeltjes vervuilen de lucht en zijn schadelijk voor de gezondheid. Inbouwen van roetfilters levert dus een bijdrage aan de verbetering van de luchtkwaliteit.<br />Een roetfilter kan bij personen- of bedrijfsauto's met een dieselmotor al tijdens het fabricageproces (ook wel 'affabriek' genoemd) van de auto worden ingebouwd. Met de modernste motortechnieken is het echter ook mogelijk om de roetuitstoot zonder roetfilter sterk te verminderen. Hoewel deze voertuigen hierbij niet daadwerkelijk voorzien worden van een roetfilter, registreert de RDW voor deze voertuigen wel een roetfilter, mits de roetuitstoot niet hoger is dan 0,005 gram/km.<br />Er zijn ook voertuigen die wel een affabriek roetfilter hebben, maar daarmee toch nog meer dan 0,005 gram/km roetdeeltjes uitstoten. De RDW registreert voor deze voertuigen dan geen Affabriek roetfilter, maar 'Nee'.<br />Een roetfilter kan ook achteraf (ook wel 'retrofit' genoemd) worden aangebracht in het uitlaatsysteem. Deze voertuigen krijgen de classificatie 'Retrofit'. De RDW registreert deze classificatie sinds medio 2006.<br />Je kunt achter het onderwerp roetfilter dus de volgende meldingen te zien krijgen:<br />• Ja Affabriek (bij dieselvoertuigen die affabriek niet meer roetdeeltjes uitstoten dan 0,005 gram/km)<br />• Ja Retrofit (bij dieselvoertuigen die achteraf (na kentekening) een roetfilter hebben gekregen)<br />• Nee (bij dieselvoertuigen zonder roetfilter of bij dieselvoertuigen met roetfilter die meer dan 0,005 gram/km roetdeeltjes uitstoten)<br />• N.v.t. (bij voertuigen die geen diesel als brandstof hebben of bij voertuigen waarvan de RDW (nog) geen roetfilters registreert)<br /><span>bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Roetfilter</strong><br/>Een roetfilter is een technische voorziening in een auto die een groot deel van de roetdeeltjes opvangt die dieselmotoren uitstoten. Die roetdeeltjes vervuilen de lucht en zijn schadelijk voor de gezondheid. Inbouwen van roetfilters levert dus een bijdrage aan de verbetering van de luchtkwaliteit.<br />Een roetfilter kan bij personen- of bedrijfsauto's met een dieselmotor al tijdens het fabricageproces (ook wel 'affabriek' genoemd) van de auto worden ingebouwd. Met de modernste motortechnieken is het echter ook mogelijk om de roetuitstoot zonder roetfilter sterk te verminderen. Hoewel deze voertuigen hierbij niet daadwerkelijk voorzien worden van een roetfilter, registreert de RDW voor deze voertuigen wel een roetfilter, mits de roetuitstoot niet hoger is dan 0,005 gram/km.<br />Er zijn ook voertuigen die wel een affabriek roetfilter hebben, maar daarmee toch nog meer dan 0,005 gram/km roetdeeltjes uitstoten. De RDW registreert voor deze voertuigen dan geen Affabriek roetfilter, maar 'Nee'.<br />Een roetfilter kan ook achteraf (ook wel 'retrofit' genoemd) worden aangebracht in het uitlaatsysteem. Deze voertuigen krijgen de classificatie 'Retrofit'. De RDW registreert deze classificatie sinds medio 2006.<br />Je kunt achter het onderwerp roetfilter dus de volgende meldingen te zien krijgen:<br />• Ja Affabriek (bij dieselvoertuigen die affabriek niet meer roetdeeltjes uitstoten dan 0,005 gram/km)<br />• Ja Retrofit (bij dieselvoertuigen die achteraf (na kentekening) een roetfilter hebben gekregen)<br />• Nee (bij dieselvoertuigen zonder roetfilter of bij dieselvoertuigen met roetfilter die meer dan 0,005 gram/km roetdeeltjes uitstoten)<br />• N.v.t. (bij voertuigen die geen diesel als brandstof hebben of bij voertuigen waarvan de RDW (nog) geen roetfilters registreert)<br /><span>bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
N.v.t.

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label" data-tooltip="<strong>Geluidsniveau rijdend</strong><br/>Het geluidsniveau van een rijdend voertuig in dB(A), gemeten zoals voorgeschreven in de regelgeving. 
Voor elektrische en plug-in hybride voertuigen wordt dit gegeven niet vastgelegd.
<span>Bron: RDW</span> ">
        Geluidsniveau rijdend
    <span data-toggle="tooltip" data-html="true" title="<strong>Geluidsniveau rijdend</strong><br/>Het geluidsniveau van een rijdend voertuig in dB(A), gemeten zoals voorgeschreven in de regelgeving. <br />Voor elektrische en plug-in hybride voertuigen wordt dit gegeven niet vastgelegd.<br /><span>Bron: RDW</span> "></span><span data-toggle="tooltip" data-html="true" title="<strong>Geluidsniveau rijdend</strong><br/>Het geluidsniveau van een rijdend voertuig in dB(A), gemeten zoals voorgeschreven in de regelgeving. <br />Voor elektrische en plug-in hybride voertuigen wordt dit gegeven niet vastgelegd.<br /><span>Bron: RDW</span> "></span></div>
    <div class="col-6 col-sm-7 value">
66 dB(A)

    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Milieusticker Duitsland
    </div>
    <div class="col-6 col-sm-7 value">
Groen

    </div>
</div>             <div class="result_title subheader">
                <h3>Milieuzones</h3>
            </div>             <div class="row multipleitemselect">
                <div class="col-12 col-sm-5">
                    <label>
                        Kies een plaats:
                        <select id="select_Kieseenplaats">
                                <option value="'s Hertogenbosch">'s Hertogenbosch</option>
                                <option value="Amsterdam">Amsterdam</option>
                                <option value="Arnhem">Arnhem</option>
                                <option value="Breda">Breda</option>
                                <option value="Delft">Delft</option>
                                <option value="Den Haag">Den Haag</option>
                                <option value="Eindhoven">Eindhoven</option>
                                <option value="Leiden">Leiden</option>
                                <option value="Maastricht">Maastricht</option>
                                <option value="Rijswijk">Rijswijk</option>
                                <option value="Rotterdam">Rotterdam</option>
                                <option value="Tilburg">Tilburg</option>
                                <option value="Utrecht">Utrecht</option>
                        </select>
                    </label>
                </div>
                <div class="col-12 col-sm-7">
                        <div data-value="'s Hertogenbosch" class="active">De gemeente 's Hertogenbosch heeft per 1 september 2007 een milieuzone. De milieuzone omvat de oude binnenstad, 't Zand en het gebied tussen de Zuid-Willemsvaart en de Aa.</div>
                        <div data-value="Amsterdam">De gemeente Amsterdam heeft per 9 oktober 2008 een milieuzone. De amsterdamse milieuzone omvat het gebied binnen de Ring A10 met enkele uitzonderingen. Stadsdeel Amsterdam-Noord is uitgezonderd omdat hier geen luchtkwaliteitsknelpunten zijn. De bedrijventerreinen RAI, De Schinkel, Cruquius, Amstel en Amstel Business Park zijn uitgezonderd omdat het vrachtverkeer dat hier komt meestal geen bestemming elders in de stad heeft.<br><br>Sinds 1 januari 2018 geldt er een milieuzone voor:<br><br>- brom- en snorfietsen. Het gaat om 2-takt en 4-takt brom- en snorfietsen met een DET van vóór 1 januari 2011. Brommers, scooters of snorfietsen met een Datum Eerste Toelating (DET) van 2010 of ouder mogen niet meer in de bebouwde kom rijden.<br>- taxi’s (M1-voertuigcode en taxiregistratie bij RDW) met een dieselmotor en een Datum Eerste Toelating (DET) van 2008 of ouder. De milieuzone geldt voor alle taxi’s, ook taxi’s die niet geregistreerd staan in Amsterdam moeten voldoen aan de eisen voordat ze de milieuzone binnen rijden.<br><br>Sinds november 2020 geldt binnen Amsterdam een groene milieuzone voor personenauto's met een dieselmotor. Personenauto's met een dieselmotor mogen alleen de milieuzone in als ze emissieklasse 4 of hoger hebben. Personenauto’s met een dieselmotor en een emissieklasse 3 of lager hebben geen toegang meer. Auto's die niet op diesel rijden zijn gewoon welkom in de milieuzone.<br><br>Binnen Amsterdam geldt een groene milieuzone voor:<br><br>- Dieselvrachtauto’s. Dat betekent dat vrachtauto’s met een dieselmotor de milieuzone alleen in mogen als ze emissieklasse 4 of hoger hebben. Vrachtauto’s die niet op diesel rijden zijn ook welkom in de milieuzone. Vrachtauto’s met een dieselmotor en een emissieklasse 3 of lager hebben geen toegang.<br>- Dieselbestelauto’s. Dat betekent dat alleen bestelauto’s met een dieselmotor en een emissieklasse 4 of hoger de milieuzone in mogen. De gemeente gaat dus niet meer uit van de Datum Eerste Toelating (DET). Bestelauto’s die niet op diesel rijden blijven welkom. Bestelauto’s met een dieselmotor en een emissieklasse 3 of lager hebben geen toegang meer.<br>- Autobussen die rijden op diesel. Dat betekent dat autobussen met een dieselmotor alleen de milieuzone in mogen als ze emissieklasse 4 of hoger hebben. De gemeente gaat dus niet meer uit van de DET. Autobussen die niet op diesel rijden blijven welkom in de milieuzone. Autobussen met een dieselmotor en emissieklasse 3 of lager hebben geen toegang meer.<br><br>Vanaf 1 januari 2022 wordt de milieuzone aangescherpt. Dan hebben dieselautobussen- en touringcars alleen toegang met emissieklasse 6 en hoger.<br>- Dieselvoertuigen, ook als deze staan geregistreerd als kampeerwagen. Dat betekent dat alleen voertuigen met een dieselmotor en een emissieklasse 4 of hoger de milieuzone in mogen. De gemeente gaat dus niet meer uit van de Datum Eerste Toelating (DET). Voertuigen die niet op diesel rijden blijven welkom. Voertuigen met een dieselmotor en een emissieklasse 3 of lager hebben geen toegang meer.<br><br>NB: in het ontheffingenbeleid van gemeente Amsterdam is vastgelegd dat bijzondere voertuigen zijn ontheven (mits niet ouder dan 13 jaar). U heeft dus geen ontheffing van RVO.nl meer nodig voor toegang tot de Amsterdamse milieuzone. U hoeft ook geen ontheffing aan te vragen bij de gemeente Amsterdam. In de praktijk verandert er voor u helemaal niks.<br>Om diezelfde reden ontbreekt Amsterdam in de opsomming van steden in de ‘Kennisgeving Ontheffingverlening Milieuzones’ waarvoor RvO ontheffing verleent.<br>    </div>
                        <div data-value="Arnhem">De gemeente Arnhem heeft per 1 juli 2014 een milieuzone voor vrachtverkeer. De Arnhemse milieuzone betreft het gebied binnen de centrumring Arnhem, inclusief de centrumring zelf.</div>
                        <div data-value="Breda">De gemeente Breda heeft per 4 oktober 2007 een milieuzone. De milieuzone omvat de binnenzijde van de singels.<br>        De Tramsingel, Oranjesingel, Wilhelminasingel en de Fellenoordstraat zijn wel toegankelijk voor alle vrachtverkeer.</div>
                        <div data-value="Delft">De gemeente Delft heeft per 1 januari 2010 een milieuzone.<br>De milieuzone omvat grofweg het gebied ten zuidoosten van de binnenstad van Delft. Hiermee draagt de milieuzone bij aan het verbeteren van de luchtkwaliteit in dit gebied. De milieuzone is zo gesitueerd dat deze de knelpunten in de luchtkwaliteit omvat en sluiproutes door woonwijken tegengaat.</div>
                        <div data-value="Den Haag">Vanaf 1 januari 2022 mogen alleen vrachtauto’s en bussen met emissieklasse 6 en voertuigen die geen schadelijke stoffen uitstoten in de milieuzone rijden. Tot 1 januari 2022 is de milieuzone nog toegestaan voor:<br>- Vrachtauto's met emissieklasse 4 of hoger.<br>- Bijzondere voertuigen die niet ouder zijn dan 13 jaar.<br><br>De milieuzone ligt binnen de Centrumring (S100) en het Telderstracé (S200).<br><br>Vanaf 1 juli 2021 vallen ook de volgende gebieden onder de milieuzone:<br>- het gebied ten noorden van de Javastraat/Laan van Meerdervoort binnen het Telderstracé.<br>- het gebied ten zuiden van de Waldorpstraat, Rijswijkseplein, en Weteringkade tot aan de Centrumring.<br><br>De volgende wegen vallen buiten de milieuzone:<br>- de Centrumring en het Telderstracé zelf.<br>- de weg vanaf de Lijnbaan naar de parkeerplaats en de parkeergarage van het ziekenhuis HMC Westeinde<br><br>NB: in het ontheffingenbeleid van gemeente Den Haag is vastgelegd dat bijzondere voertuigen zijn ontheven (mits niet ouder dan 13 jaar). U heeft dus geen ontheffing van RVO.nl meer nodig voor toegang tot de Haagse milieuzone. U hoeft ook geen ontheffing aan te vragen bij de gemeente Den Haag. In de praktijk verandert er voor u helemaal niks.</div>
                        <div data-value="Eindhoven">De gemeente Eindhoven heeft per 1 juli 2007 een milieuzone. De eindhovense milieuzone omvat het gebied binnen de ring (postcodegebied 5611 tot en met 5616), met uitzondering van bedrijventerrein De Kade.</div>
                        <div data-value="Leiden">De gemeente Leiden heeft per 1 januari 2010 een milieuzone. De leidse milieuzone omvat het gebied binnen de singels en het oostelijke deel van de Morsweg.</div>
                        <div data-value="Maastricht">De gemeente Maastricht heeft per 1 maart 2010 een milieuzone. De milieuzone omvat de Statensingel.</div>
                        <div data-value="Rijswijk">De gemeente Rijswijk heeft per 1 november 2010 een milieuzone. De rijswijkse milieuzone omvat het gebied tussen de Burgemeester Elsenlaan, de stadgrenzen met Den Haag en Voorburg, De Vliet tot aan de Prunuskade en via de Handelskade tot aan de Burgemeester Elsenlaan. Een deel van de Rotterdamseweg, tot aan de Laan van Oversteen, valt ook binnen de zone.</div>
                        <div data-value="Rotterdam">De gemeente Rotterdam heeft per 16 september 2007 een milieuzone. De Rotterdamse milieuzone omvatte tot voor kort in grote lijnen het CS-kwartier, de Stadsdriehoek, het Oude Westen en de wijk Cool.<br><br>Per 1 januari 2016 heeft de gemeente Rotterdam de milieuzone uitgebreid. De zone is groter geworden. De milieuzone ligt grofweg binnen de ‘ruit’ van Rotterdam, aan de noordkant van de Maas. De milieuzone ligt in het centrum en het noorden van de stad, tussen de A20, de A16, de Nieuwe Maas en de S114 (Tjalklaan, Vierhavenstraat, Westzeedijk). De drie oeververbindingen Maastunnel, Erasmusbrug en Willemsbrug (inclusief Noordereiland) liggen ook in de milieuzone. Op de kaart hieronder geeft de zwarte lijn de grens van de milieuzone aan.<br><br>Naast de geografische uitbreiding is de milieuzone ook gaan gelden voor bestelauto’s en personenauto’s.<br><br>NB: in het ontheffingenbeleid van de gemeente Rotterdam is vastgelegd dat bijzondere voertuigen zijn ontheven (mits niet ouder dan 13 jaar). U heeft dus geen ontheffing van RVO.nl meer nodig voor toegang tot de Rotterdamse milieuzone. U hoeft ook geen ontheffing aan te vragen bij de gemeente Rotterdam. In de praktijk verandert er voor u helemaal niks.<br>Om diezelfde reden ontbreekt Rotterdam in de opsomming van steden in de ‘Kennisgeving Ontheffingverlening Milieuzones’ waarvoor RvO ontheffing verleent.</div>
                        <div data-value="Tilburg">De gemeente Tilburg heeft sinds 1 september 2007 een milieuzone. De Tilburgse milieuzone bestrijkt het gebied binnen de ringbanen.</div>
                        <div data-value="Utrecht">De gemeente 's Utrecht heeft per 1 juli 2007 een milieuzone. De milieuzone omvat de gehele binnenstad, het stationsgebied, de Jaarbeurs en enkele aangrenzende wegen.</div>
                </div>
            </div>


<div class="col-12 col-sm-12">
    <div class="row center">
        <div class="col-12 col-sm-5">
            <a href="https://www.autooverdegrens.nl/?utm_source=finnik&amp;utm_medium=link" class="button external" target="_blank" data-event="buttonenvironmental_sticker">Milieusticker Duitsland of Frankrijk<span></span></a>
        </div>
    </div>
</div>

</section>            <!-- Autozine  -->



<section class="result stickytitle">
    <div class="result_title">
        <h3>Beoordeling door Autozine</h3>
        <p>Beoordeling door Autozine; hét Automagazine op internet</p>
    <a href="#" class="backtotop"></a></div>

    <div class="autozine row">
        <div class="col-12 col-sm-6">
                <img src="https://www2.autozine.nl/cache/simplescale/728/20179.jpg" loading="lazy">
        </div>

        <div class="col-12 col-sm-6">
                        <div class="row">
                            <div class="col-12 col-sm-6">
                                <div class="result_value positive">
                                    Pluspunten
                                </div>
                                <ul>
                                        <li>Geen (directe) uitstoot<br></li>
                                        <li>Overtuigend premium-gevoel<br></li>
                                        <li>Levendig karakter<br></li>
                                </ul>
                            </div>
                            <div class="col-12 col-sm-6">
                                <div class="result_value negative">
                                    Minpunten
                                </div>
                                <ul class="negative">
                                        <li>A-stijl hindert zicht (afhankelijk van postuur bestuurder)<br></li>
                                        <li>Matige beenruimte achterin<br></li>
                                </ul>
                            </div>
                        </div>

    <div class="row">
        <div class="col-12 label">
            De elektrische i3 rijdt als een echte BMW en heeft dezelfde premium kwaliteit. Daarbij is de i3 een pionier op het gebied van milieuvriendelijk bouwen. Goed nieuws voor het milieu en autoliefhebbers.
        </div>
    </div>
                        <div class="row">
                            <div class="col-12 col-sm-12">
                                

<a class="reviewlink" rel="nofollow" href="https://www.autozine.nl/bmw/i3/electric-60-ah/autotest" target="_blank" data-event="linkautozine.nl">Lees het volledige verslag hier</a>
                            </div>
                        </div>        </div>
    </div>
</section>            <!-- FunFacts  -->

<section class="result stickytitle">
    <div class="result_title">
        <h3><a id="funfacts" data-title="Fun Facts"></a>Fun Facts</h3>
        <p>Interessante feitjes. Leuk voor op een feestje</p>
    <a href="#" class="backtotop"></a></div>
    <div class="row">
        


                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon calendar" data-origbgimage="url(&quot;https://finnik.nl/svg/calendar/405E7A.svg&quot;)">
                        Gem. 618 dagen in bezit per eigenaar
                    </div>
                </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon colorpalette" data-origbgimage="url(&quot;https://finnik.nl/svg/colorpalette/405E7A.svg&quot;)">
                        3.138.896 voertuigen van deze kleur
                    </div>
                </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon gender" data-origbgimage="url(&quot;https://finnik.nl/svg/gender/405E7A.svg&quot;)">
                        36% van de bezitters is vrouw
                    </div>
                </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon cars" data-origbgimage="url(&quot;https://finnik.nl/svg/cars/405E7A.svg&quot;)">
                        Er zijn 9.481 voertuigen van dit merk/model in NL
                    </div>
                </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon cars" data-origbgimage="url(&quot;https://finnik.nl/svg/cars/405E7A.svg&quot;)">
                        Er waren vorig jaar 1.684 voertuigen van dezelfde uitvoering in NL
                    </div>
                </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon speed" data-origbgimage="url(&quot;https://finnik.nl/svg/speed/405E7A.svg&quot;)">
                        956.122 voertuigen sneller of meer PK
                    </div>
                </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon cake" data-origbgimage="url(&quot;https://finnik.nl/svg/cake/405E7A.svg&quot;)">
                        De gemiddelde eigenaar is 54 jaar oud
                    </div>
                </div>
                <div class="col-sm-6 col-md-4 mb-4">
                    <div class="icon crosshairs" data-origbgimage="url(&quot;https://finnik.nl/svg/crosshairs/405E7A.svg&quot;)">
                        Dit kenteken is 9 keer gespot
                    </div>
                </div>


    </div>
</section>            <!-- Automarkt  -->

<section class="result stickytitle" data-sectiontype="Automarkt">
    <div class="result_title">
        <h3><a id="automarkt" data-title="Automarkt"></a>Automarkt

</h3>
        <p>(Ver)kopen via AutoScout24 en onze eigen markt</p>
    <a href="#" class="backtotop"></a></div>

    


            <div class="result_title subheader">
                <h3>Koop dit type auto (171 te koop)</h3>
            </div> 

<div class="row">
    <div class="col-6 col-sm-5 label withbutton">
            <img loading="lazy" src="https://finfabackendprodstorage.blob.core.windows.net/images/autoscout24logo2x1.png" alt="" style="">
    </div>
    <div class="col-6 col-sm-5">
        
<a href="https://www.autoscout24.nl/lst/BMW/i3?sort=standard&amp;desc=0&amp;cy=NL&amp;utm_source=finnik_app&amp;utm_campaign=buy&amp;utm_medium=co&amp;utm_term=list&amp;utm_content=textbutton" target="_blank" class="button external" data-targethost="autoscout24.nl" data-event="buttonExternal">Koop via AutoScout24</a>
    </div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label withbutton">
            <img loading="lazy" src="https://finfabackendprodstorage.blob.core.windows.net/images/finniklogo.png" alt="" style="">
    </div>
    <div class="col-6 col-sm-5">
        
<a href="https://automarkt.finnik.nl/automarkt/?brand=BMW&amp;serie=i3" target="_blank" class="button external" data-targethost="automarkt.finnik.nl" data-event="buttonExternal">Koop via Finnik</a>
    </div>
</div>            <div class="result_title subheader">
                <h3>Verkoop je auto</h3>
            </div> 

<div class="row">
    <div class="col-6 col-sm-5 label withbutton">
            <img loading="lazy" src="https://finfabackendprodstorage.blob.core.windows.net/images/finnikfairkochtlogo.png" alt="" style="">
    </div>
    <div class="col-6 col-sm-5">
        
<a href="https://fairkocht.online/?utm_source=finnik&amp;utm_medium=button" target="_blank" class="button external" data-targethost="fairkocht.online" data-event="buttonExternal">Verkoop je auto vanuit je luie stoel</a>
    </div>
</div>

<div class="row">
    <div class="col-6 col-sm-5 label withbutton">
            <img loading="lazy" src="https://finfabackendprodstorage.blob.core.windows.net/images/autoscout24logo2x1.png" alt="" style="">
    </div>
    <div class="col-6 col-sm-5">
        
<a href="https://www.autoscout24.nl/auto-verkopen/?utm_source=finnik_app&amp;utm_campaign=sell&amp;utm_medium=co&amp;utm_term=insertion&amp;utm_content=textbutton" target="_blank" class="button external" data-targethost="autoscout24.nl" data-event="buttonExternal">Verkoop je auto gratis</a>
    </div>
</div>            <div class="result_title subheader">
                <h3>Deze auto financieren</h3>
            </div> 

<div class="row">
    <div class="col-6 col-sm-5 label withbutton">
            <img loading="lazy" src="https://finfabackendprodstorage.blob.core.windows.net/images/dmfkredietlogo.png" alt="" style="">
    </div>
    <div class="col-6 col-sm-5">
        
<a href="https://finnik.nl/goto/dmfkrediet-offerte-autorapport/h532dt/BMW/i3" target="_blank" class="button external" data-targethost="finnik.nl" data-event="buttonExternal">Financieren via DMF krediet</a>
    </div>
</div>

</section>            <!-- TheftCheck  -->

<section class="result stickytitle" data-sectiontype="TheftCheck">
    <div class="result_title">
        <h3><a id="diefstalcheck" data-title="Diefstalcheck"></a>Diefstalcheck

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="TheftCheck" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
</h3>
        <p>Diefstalinformatie en -prognose</p>
    <a href="#" class="backtotop"></a></div>

    




    <div class="row">
        <div class="col-12 label">
             • 1 op 5 auto's heeft een bovengemiddeld of hoog risico op diefstal <br> • 1 op 1000 auto's gebouwd in de laatste 10 jaar is gestolen in het afgelopen jaar
        </div>
    </div>


<div class="row">
    <div class="col-6 col-sm-5 label">
        Uitvoeringen gestolen vorig jaar
    </div>
    <div class="col-6 col-sm-7 value">
••••••

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="Uitvoeringen gestolen vorig jaar" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Diefstalrisico komend jaar
    </div>
    <div class="col-6 col-sm-7 value">
••••••

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="Diefstalrisico komend jaar" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
    </div>
</div> 

<div class="row">
    <div class="col-6 col-sm-5 label">
        Diefstalverhogende factoren
    </div>
    <div class="col-6 col-sm-7 value">
••••••

    <a href="/checkout/h532dt" class="lock buypremium" title="Koop premiumrapport" data-event="premiumLock" data-celltitle="Diefstalverhogende factoren" data-origbgimage="url(&quot;https://finnik.nl/svg/lock/00ada8.svg&quot;)"></a>
    </div>
</div> 

</section>            <!-- Banner  -->


<div class="row center">
    <div class="col-12 col-sm-8 col-md-5 mb-4 col-lg-5 col-xl-4">
        <a ref="nofollow" href="https://finnik.nl/goto/mijnautocoach" target="_blank" data-event="bannerClick">
            <img class="promo" src="https://finfabackendprodstorage.blob.core.windows.net/images/mijnautocoachbanner.jpg" loading="lazy">
        </a>
        <p><a href="/checkout/h532dt">Koop een premium en krijg een jaar zonder reclame</a></p>
    </div>
</div><section class="result noprint">
    <div class="result_title">
        <h3>Hoe bevalt Finnik u?</h3>
        <p>Laat ons weten hoe u ons beoordeelt.</p>
    </div>
    <div>
        <div class="row">
            <div class="col-12">
                <div class="starcontainer">
                    <div class="stars center">
                        <div class="icon star" data-toggle="tooltip" data-original-title="Slecht" data-origbgimage="url(&quot;https://finnik.nl/svg/star/405E7A.svg&quot;)"></div>
                        <div class="icon star" data-toggle="tooltip" data-original-title="Matig" data-origbgimage="url(&quot;https://finnik.nl/svg/star/405E7A.svg&quot;)"></div>
                        <div class="icon star" data-toggle="tooltip" data-original-title="Redelijk" data-origbgimage="url(&quot;https://finnik.nl/svg/star/405E7A.svg&quot;)"></div>
                        <div class="icon star" data-toggle="tooltip" data-original-title="Goed" data-origbgimage="url(&quot;https://finnik.nl/svg/star/405E7A.svg&quot;)"></div>
                        <div class="icon star perfect" data-toggle="tooltip" data-original-title="Uitstekend" data-origbgimage="url(&quot;https://finnik.nl/svg/star/405E7A.svg&quot;)"></div>
                    </div>
                    <p id="startext" style="text-align: center;"></p>
                    <div style="clear: both;"></div>
                </div>
                <div id="ratedlow">
                    <p>Bedankt voor uw waardering! Dat kan dus beter. Gaat er iets mis of heeft u een idee over wat we beter kunnen doen? Laat het ons weten! Met uw feedback kunnen we Finnik beter maken.</p>
                    <div class="row center">
                        <div class="col-12 col-sm-5">
                            <p><a href="#" class="button noload" data-open="feedbackform">Geef feedback</a></p>
                        </div>
                    </div>
                </div>
                <div id="ratedperfect">
                    <p>Bedankt voor uw waardering! Zou u een (korte) recensie willen achterlaten bij Google? Op deze manier kan Finnik meer mensen helpen. Alvast bedankt!</p>
                    <div class="row center">
                        <div class="col-12 col-sm-5">
                            <a href="https://www.google.com/search?q=finnik&amp;rlz=1C1GCEA_enNL932NL932&amp;oq=finnik&amp;aqs=chrome..69i64j35i39j0i131i433i512j0i512l2j69i60l3.1720j0j1&amp;sourceid=chrome&amp;ie=UTF-8#lrd=0x47c5e1894bd88e31:0x697e7888543d7f53,1,,," target="_blank" class="button external" data-event="googlereview">Laat recensie achter</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
        <div class="container">
            <div class="row center noprint">
                <div class="col-12 col-md-5 text-center">
                    <p><a href="https://finnik.nl/kenteken/h532dt.pdf" target="_blank" class="button alt noload" data-event="downloadPdf">Download rapport als PDF</a></p>
                </div>
            </div>
            <div class="row center noprint">
                <div class="col-12 col-md-5 text-center">
                    <p><a href="#" class="button alt noload" data-open="feedbackform">Support</a></p>
                </div>
            </div>
            <div class="row center noprint">
                <div class="col-12 col-md-5">
                    
<div class="card-kenteken">
    <div class="card-body-kenteken">
        <div class="text-center">
            <img src="/content/assets/logo.svg" loading="lazy" alt="Finnik logo" class="logo" width="200" height="86">
        </div>
<form action="/kenteken/index" class="licenseplateform" data-url="/kenteken/" method="get">            <div class="input-group mb-3">
                <div class="input-group-append">
                    <button class="licenseplatesearch btn-search-reverse" type="button" data-event="searchglassButton">
                        <img src="/content/assets/glass2.svg" loading="lazy" class="glass" alt="search" width="16" height="16">
                    </button>
                    <input type="text" name="licensePlateNumber" class="licenseplateinput form-control-search-reverse" autocomplete="off" placeholder="XX-123-X" maxlength="10">
                </div>
                <div class="history">
                    <ul>
                    <li><a href="/kenteken/h532td" class="licenseplate" data-event="licenseplate_autofill_history">H-532-TD</a></li><li><a href="/kenteken/65zgxk" class="licenseplate" data-event="licenseplate_autofill_history">65-ZG-XK</a></li><li><a href="/kenteken/hs830v" class="licenseplate" data-event="licenseplate_autofill_history">HS-830-V</a></li></ul>
                </div>
            </div>
            <button class="licenseplatesearch button">Zoek kenteken</button>
</form>    </div>
</div>
                </div>
            </div>
        </div>



<section id="premiumBanner" style="bottom: -1px;">
    <div class="carkenteken">
        <img loading="lazy" src="https://pictures.vwe.nl/ATL/bmw/ATX_M2547_F2.jpg" alt="Premium Kentekencheck BMW i3" class="car_picture" onabort="CarPlaceHolderImageUrl" onerror="this.onerror=null;this.src='/Content/assets/car-image-placeholder.svg';">
        <div>
            <p class="only_mobile">
                <span class="title">Basisrapport</span>
            </p>
            <p class="only_desktop">
                <span>BMW i3 Executive Edition 120Ah 42 kWh</span>
            </p>
            <span class="licenseplate">H-532-DT</span>
        </div>

        <a href="/checkout/h532dt" class="button only_mobile buypremium noload" data-event="premiumBottom">Bekijk alle data</a>
        <a href="/checkout/h532dt" class="button only_desktop buypremium noload" data-event="premiumBottom">Bekijk alle data</a>
    </div>
</section></main>

    <div class="carreportbottom mt-5">
        <div class="vwelogo"></div>
    </div>

    <div class="modal fade wide" id="checkoutModal" tabindex="-1" role="dialog" aria-labelledby="checkoutModalLabel" style="display: none;" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content col-12">
                <div class="modal-header">
                    <a href="#" class="close" data-dismiss="modal" aria-label="Close"></a>

                    <div class="row center mb-0 pb-0">
                        <h1 class="center h1">Premium Kentekencheck</h1>
                    </div>
                </div>
                <div class="modal-body">
                    <div class="row center mt-0 pt-0">
                        <p class="mb-0">Je staat op het punt om een premiumrapport te kopen voor het volgende kenteken:</p>
                    </div>
                    <div class="row center mt-3">
                        <div class="licenseplate large">H-532-DT</div>
                    </div>
                    <div id="paymentdetails">


    <div class="row center">
        <div class="col-12 col-sm-8 col-md-6 mt-4">
            <a href="/betaling/premium/h532dt" class="button " data-event="paymentButton">Koop Premiumrapport voor € 3,99</a>
        </div>
    </div>
        <p class="worddivide mt-3 mb-4">OF</p>
        <div id="bundleinformation">
            <div class="center">Koop een bundel en bespaar!</div>
            <div class="value_items">
                <div class="row center mb-1">
                        <a href="/betaling/bundel/h532dt/3" class="col-12 col-sm-8 col-md-3 mb-2 mx-1 pt-4 mb-md-0 result option" data-event="checkoutBundleClick" data-productcode="spot_premium_bundle_3">
                            
                            <div>
                                <h3>3 Premiums</h3>
                                <span style="text-decoration: line-through;">€ 11,97</span>
                                <br>
                                <span>€ 9,99</span>
                            </div>
                        </a>
                        <a href="/betaling/bundel/h532dt/6" class="col-12 col-sm-8 col-md-3 mb-2 mx-1 pt-4 mb-md-0 result option" data-event="checkoutBundleClick" data-productcode="spot_premium_bundle_6">
                            
                                 <div class="ribbon"><span>Populair</span></div>
                            <div>
                                <h3>6 Premiums</h3>
                                <span style="text-decoration: line-through;">€ 23,94</span>
                                <br>
                                <span>€ 17,99</span>
                            </div>
                        </a>
                        <a href="/betaling/bundel/h532dt/50" class="col-12 col-sm-8 col-md-3 mb-2 mx-1 pt-4 mb-md-0 result option" data-event="checkoutBundleClick" data-productcode="spot_premium_bundle_50">
                            
                                <div class="ribbon green"><span>Groen*</span></div>
                                <div class="moreinfo">
                                </div>
                            <div>
                                <h3>50 Premiums</h3>
                                <span style="text-decoration: line-through;">€ 199,50</span>
                                <br>
                                <span>€ 99,99</span>
                            </div>
                        </a>
                </div>
            </div>
            <div class="center">
                <p>* Voor elke 50-bundel plant Finnik een boom. <a href="#woodyoucare">Meer informatie</a>.</p>
            </div>
        </div>

</div>
                    <div class="text-center result_title pb-md-3 mt-2">
                        <p>Heb je een vouchercode? <a href="#" data-toggle="modal" data-target="#voucherModal">Vul in!</a></p>
                        <p><a target="_blank" href="/algemenevoorwaarden">Algemene voorwaarden</a> van toepassing.</p>
                    </div>
                    <div class="value_items">
                        <div class="row">
                        
                                    <div class="col-12 col-md-6 mb-4">
                                        <h3><img src="/svg/checkmark/72bc22.svg" width="24" height="24"> Wacht Op Keuren (WOK)</h3>
                                        Zoek uit of dit voertuig voldoet aan de wettelijke eisen of dat het nog moet wachten op een keuring.
                                    </div>
                                    <div class="col-12 col-md-6 mb-4">
                                        <h3><img src="/svg/checkmark/72bc22.svg" width="24" height="24"> Elektrische informatie</h3>
                                        Alle elektrische informatie over deze auto. Zie de actieradius, verbruik, vermogen, laadtijd, laadsnelheid en veel meer!
                                    </div>
                                    <div class="col-12 col-md-6 mb-4">
                                        <h3><img src="/svg/checkmark/72bc22.svg" width="24" height="24"> Opties en accessoires</h3>
                                        Alle opties en accessoires die van toepassing zijn op de auto. Geen reden om te gissen met een Premium Kentekecheck.
                                    </div>
                                    <div class="col-12 col-md-6 mb-4">
                                        <h3><img src="/svg/checkmark/72bc22.svg" width="24" height="24"> Total Cost of Ownership</h3>
                                        Geeft inzicht in de kosten voor het onderhoud, afschrijving, brandstof, banden en wegenbelasting op voertuigniveau.
                                    </div>
                                    <div class="col-12 col-md-6 mb-4">
                                        <h3><img src="/svg/checkmark/72bc22.svg" width="24" height="24"> Exacte waarde</h3>
                                        Met de exacte waarde van de auto, weet je precies waar je aan toe bent. Of je nou een auto koopt of verkoopt.
                                    </div>
                                    <div class="col-12 col-md-6 mb-4">
                                        <h3><img src="/svg/checkmark/72bc22.svg" width="24" height="24"> Diefstalcheck</h3>
                                        Zie hoeveel van deze auto's het afgelopen jaar zijn gestolen en wat onze voorspelling is voor het komende jaar. Plus meer!
                                    </div>
                        </div>
                    </div>
                    <div class="text-center result_title py-3">
                        <a target="_blank" href="/kenteken/ht260x">Bekijk hier een voorbeeld van een premiumrapport</a>
                    </div>
                        <div class="row center mb-3">
                            <div class="col-12 col-sm-8 col-md-6 mt-4">
                                <a href="/betaling/premium/h532dt" class="button " data-event="paymentButton">Koop Premiumrapport voor € 3,99</a>
                            </div>
                        </div>
                    <div class="center">
                            <a href="/betaling/premium/h532dt?method=ideal" class="icon ideal" data-event="add_payment_info"></a>
                            <a href="/betaling/premium/h532dt?method=paypal" class="icon paypal" data-event="add_payment_info"></a>
                            <a href="/betaling/premium/h532dt?method=creditcard" class="icon mastercard" data-event="add_payment_info"></a>
                            <a href="/betaling/premium/h532dt?method=creditcard" class="icon visa" data-event="add_payment_info"></a>
                    </div>
                    <div class="row center divide pt-4">
                        <div class="col-12 col-sm-3">
                            <a id="woodyoucare"></a>
                            <a href="https://woodyou.care/companies/finnik" target="_blank">
                                <img src="/Content/icons/woodyoucare_vwe_bronze.png" height="180" style="background: white; border-radius: 23px;">
                            </a>
                        </div>
                        <div class="col-12 col-sm-6 text-left">
                            <h2>WoodYouCare</h2>
                            <p>Finnik werkt samen met <a href="https://woodyou.care/">WoodYouCare</a> en plant een boom voor elke 50-bundel die wordt verkocht.</p>
                                <p>Er zijn tot op heden <strong>72</strong> bomen geplant, en dit compenseert 1703,79 kg CO2 per jaar. </p>
                        </div>
                    </div>
                </div>
                <div class="modal-footer"></div>
            </div>
        </div>
    </div>
    

</body></html>"""


class TestFinnikOnlineClient(TestCase):

    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    @classmethod
    def setUpClass(cls):
        cls.finnik_client = FinnikOnlineClient()

    def test_invalid_too_long(self):
        with self.assertRaises(AssertionError) as e:
            self.finnik_client.get_car_details('tooLong')
            assert str(e.exception) == 'Length of the licence plate must be 6 (without any dashes).'

    @mock.patch('requests.get')
    def test_getting_success_response(self, mock_requests):
        mock_requests.return_value = self._mock_response(content=FINNIK_RES_DATA)
        assert self.finnik_client.get_car_details('ab123z') == {
            'brand': "BMW",
            'model': "i3",
            'apk': "31-12-2023",
            'price': 46660,
            'acceleration': "7.3",
            'bpm': 123456
        }
    @mock.patch('requests.get')
    def test_not_found(self, mock_requests):
        mock_requests.return_value = self._mock_response()
        details = self.finnik_client.get_car_details('ab123z')
        self.assertIsNone(details)

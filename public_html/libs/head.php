<?php
if (!defined('ABSPATH')) {
    $wp_load = dirname(__DIR__) . '/wp/wp-load.php';
    if (file_exists($wp_load)) {
        require_once $wp_load;
    }
}

global $post;

$title       = '';
$description = '';
$url         = '';
$thumb       = defined('APP_URL') ? APP_URL . 'assets/images/default/og-image.jpg' : '/assets/images/default/og-image.jpg';

if ( function_exists('is_front_page') && (is_front_page() || is_home()) ) {
    // Trang chủ
    $title       = get_bloginfo('name');
    $description = get_bloginfo('description');
    $url         = home_url('/');
} elseif ( function_exists('is_singular') && is_singular() ) {
    // Bài viết / trang đơn
    $post_id     = get_the_ID();
    $title       = get_the_title($post_id);
    $description = wp_strip_all_tags(get_the_excerpt($post_id));
    $url         = get_permalink($post_id);
    $post_thumb  = get_the_post_thumbnail_url($post_id, 'full');
    if ($post_thumb) {
        $thumb = $post_thumb;
    }
} elseif ( function_exists('is_category') && (is_category() || is_tag() || is_tax()) ) {
    // Trang danh mục / tag
    $term        = get_queried_object();
    $title       = ($term && isset($term->name)) ? $term->name . ' - ' . get_bloginfo('name') : get_bloginfo('name');
    $description = ($term && !empty($term->description)) ? $term->description : get_bloginfo('description');
    $url         = ($term) ? get_term_link($term) : home_url('/');
} else {
    // Fallback
    $title       = function_exists('get_bloginfo') ? get_bloginfo('name') : 'EBO - Giải pháp Website, Marketing Online';
    $description = function_exists('get_bloginfo') ? get_bloginfo('description') : '';
    $url         = function_exists('home_url') ? home_url('/') : 'https://ebo.com.vn/';
}
?>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
    
    <title><?php echo ($title) ? esc_html($title) : "EBO - Giải pháp Website, Marketing Online cho doanh nghiệp"; ?></title>
    
    <meta name="description" content="<?php echo esc_attr($description); ?>">
    <meta name="keywords" content="seo, website, ebo">

    <meta property="og:title" content="<?php echo esc_attr($title); ?>">
    <meta property="og:type" content="website">
    <meta property="og:url" content="<?php echo esc_url($url); ?>">
    <meta property="og:image" content="<?php echo esc_url($thumb); ?>">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="<?php echo function_exists('get_bloginfo') ? esc_attr(get_bloginfo('name')) : 'EBO'; ?>">
    <meta property="og:description" content="<?php echo esc_attr($description); ?>">
    <meta property="fb:app_id" content="">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="<?php echo esc_url($url); ?>">
    <meta name="twitter:title" content="<?php echo esc_attr($title); ?>">
    <meta name="twitter:description" content="<?php echo esc_attr($description); ?>">
    <meta name="twitter:image" content="<?php echo esc_url($thumb); ?>">

    <link href="<?php echo defined('APP_ASSETS') ? APP_ASSETS : '/assets/'; ?>css/style.css" rel="stylesheet" media="all">
    
    <link rel="icon" href="<?php echo defined('APP_URL') ? APP_URL : '/'; ?>assets/images/default/logo_d.svg" type="image/svg+xml">
    <link rel="alternate icon" href="<?php echo defined('APP_URL') ? APP_URL : '/'; ?>assets/images/default/logo_d.svg">

    <?php if (function_exists('wp_head')) { wp_head(); } ?>

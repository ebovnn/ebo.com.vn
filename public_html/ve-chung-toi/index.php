<?php
include_once(dirname(__DIR__) . '/app_config.php');
if (!defined('ABSPATH')) {
    require_once dirname(__DIR__) . '/wp/wp-load.php';
}
include(APP_PATH.'libs/head.php');
?>
</head>
<body>
<!-- HEADER -->
<?php include(APP_PATH.'libs/header.php'); ?>
<div id="app">
  <main>
    <div class="subpage-mainvisual">
      <h1 class="sub-visual-title">VỀ CHÚNG TÔI</h1>
      <div id="page-title-particles-js" class="particles-js" data-particles-type="hexagons" data-particles-number="15" data-particles-line="false" data-particles-size="5" data-particles-speed="2" data-particles-hover="false" data-particles-hover-mode="bubble" data-particles-colors-type="random_colors" data-particles-color="#ff7e00,#3224e9,#69e9f2"><canvas class="particles-js-canvas-el" width="1315" height="220" style="width: 100%; height: 100%;"></canvas></div>
    </div>

    <section class="section-timeline">
      <div id="particles_5ee8e735266a1" class="particles-js" data-particles-type="hexagons" data-particles-number="10" data-particles-color="#ff7e00,#3224e9,#69e9f2" data-particles-line="false" data-particles-size="10" data-particles-speed="1" data-particles-hover="false" data-particles-hover-mode="grab" data-particles-colors-type="random_colors"><canvas class="particles-js-canvas-el" style="width: 100%; height: 100%;" width="395" height="1309"></canvas></div>
      <div class="container">
        <h2 class="primary-title">Câu chuyện của EBO</h2>
        <div class="primary-description">Chúng tôi điều chỉnh các chiến lược của mình để cung cấp cho mọi khách hàng những giải pháp tốt nhất.</div>
        <div class="timeline-box">
          <div class="timeline-item">
            <div class="timeline-item-date aos-init" data-aos="fade-right"><p class="date">2020</p></div>
            <div class="timeline-item-content aos-init" data-aos="fade-left">
              <p><i class="far fa-check-circle"></i><span>Chú trọng về giải pháp hệ thống khách hàng.</span></p>
              <p><i class="far fa-check-circle"></i><span>Có đầy đủ nhân sự và dịch vụ để hỗ trợ khách hàng phát triển mảng online.</span></p>
              <p><i class="far fa-check-circle"></i><span>Có đầy đủ nhân sự và công cụ để hỗ trợ khách hàng số hoá các công việc doanh nghiệp</span></p>
              <p><i class="far fa-check-circle"></i><span>Luôn giữ mục tiêu "Sự phát triển của khách hàng là sự phát triển của EBO".</span></p>
            </div>  
          </div>
          <div class="timeline-item">
            <div class="timeline-item-date aos-init" data-aos="fade-right"><p class="date">2019 - 2016</p></div>
            <div class="timeline-item-content aos-init" data-aos="fade-left">
              <p><i class="far fa-check-circle"></i><span>Tập trung xử lý các yêu cầu khách hàng và tối ưu hệ thống quản lý back-end.</span></p>
            </div>  
          </div>
          <div class="timeline-item">
            <div class="timeline-item-date aos-init" data-aos="fade-right"><p class="date">2015</p></div>
            <div class="timeline-item-content aos-init" data-aos="fade-left">
              <p><i class="far fa-check-circle"></i><span>Cùng chung mục tiêu "Sự phát triển của khách hàng là sự phát triển của EBO".</span></p>
            </div>  
          </div>
        </div>
      </div>
    </section>

    <section class="section-testimonials">
      <div class="container">
        <?php include(APP_PATH.'libs/feedback.php'); ?>
      </div>
    </section>
  </main>
</div><!-- #wrap -->
<!-- FOOTER -->
<?php include(APP_PATH.'libs/footer.php'); ?>
<script>
  AOS.init();
</script>
</body>
</html>

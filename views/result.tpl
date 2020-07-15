% rebase('base.tpl', title='YOLO Result')

<div class="resultwrapper">
    <a href='/predictions/{{file}}' download><img src='/predictions/{{file}}' /></a>
    <!-- use redirect to delete image before going back home -->
    <button id="backhome" onclick="window.location='/del/{{file}}'">
        <i class="fa fa-arrow-circle-left" aria-hidden="true"></i>
    </button>
</div>

<!-- Only visible if no objects were detected -->

<div id="errorModal" class="modal">
    <div class="modal-content">
        <span onclick="closeModal()" class="close">&times;</span>
        <p>Sorry, YOLO didn't find any objects.</p>
    </div>
</div>

% if error:
<script>
    var modal = document.getElementById("errorModal");
    modal.style.display = "block";
</script>
% end
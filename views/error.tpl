% rebase('base.tpl', title='YOLO Result')

% if error == '404':
<h3 class="subtitle">Sorry, the page you're looking for is not retrievable from the
    <a class="errorlink" href="https://pjreddie.com/darknet/" rel="noopener">darknet</a>.
    <br>
    <hr>
    <a class="errorlink" href="#" onclick="goHome()">Here's</a> the homepage.
</h3>

% elif error == '500':
<h3 class="subtitle">Sorry, an unforeseen error occurred.
    <br>
    <hr>
    Please,
    <a class="errorlink" href="#" onclick="goHome()">go back</a>
    an try again.
</h3>

% elif error == '418':
<h3 class="subtitle">Sorry, I'm a teapot (jpg, jpeg, png) who refuses to brew coffee (whatever other file you gave me)!
    <br>
    <hr>
    Please,
    <a class="errorlink" href="#" onclick="goHome()">go back</a>
    an try your luck with an <i>image</i>.
</h3>

% else:
<h3 class="subtitle">Sorry, this doesn't work.
    <br>
    <hr>
    Maybe the
    <a class="errorlink" href="#" onclick="goHome()">homepage</a>
    does.

</h3>

% end
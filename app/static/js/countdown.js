// Kudos to CMS,
// http://stackoverflow.com/questions/1191865/code-for-a-simple-javascript-countdown-timer
function Countdown(options) {
    var timer,
    instance = this,
    seconds = options.seconds || 5,
    counterStart = options.onCounterStart || function() {},
    updateStatus = options.onUpdateStatus || function() {},
    counterEnd = options.onCounterEnd || function() {};

    function decrementCounter() {
        updateStatus(seconds);
        if (seconds === 0) {
            counterEnd();
            instance.stop();
        }
        seconds--;
    }

    this.start = function() {
        counterStart();
        clearInterval(timer);
        timer = 0;
        timer = setInterval(decrementCounter, 1000);
    };

    this.stop = function() {
        clearInterval(timer);
    };
}
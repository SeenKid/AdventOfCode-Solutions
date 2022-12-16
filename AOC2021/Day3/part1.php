<?php
$input = file_get_contents("input.txt");
$handle = fopen("input.txt", "r");
if ($handle) {
    $answer = 0;
    $gamma_rates = '';
    $epsilon_rates = '';

    $data_array = [];
    while (($data = fgets($handle)) !== false) {
        $data = preg_replace("/\r|\n/", "", $data);
        $data_array[] = $data;
    }

fclose($handle);

    $total = count($data_array);
    $zero_counts = [];

    for ($i = 0; $i < strlen($data_array[0]); $i++) {
        $zero_counts[$i] = 0;
    }

for ($i = 0; $i < $total; $i++) {
    $data = $data_array[$i];

    for ($j = 0; $j < strlen($data); $j++) {
        if (empty($data[$j])) {
            $zero_counts[$j]++;
        }
    }
}

for ($i = 0; $i < count($zero_counts); $i++) {
    if ($zero_counts[$i] > ($total / 2)) {
        $gamma_rates .= '0';
        $epsilon_rates .= '1';
    } else {
        $gamma_rates .= '1';
        $epsilon_rates .= '0';
    }
}
/* echo "gamma_rates:" . bindec($gamma_rates) . "\n";
echo "epsilon_rates:" . bindec($epsilon_rates) . "\n"; */
$answer = bindec($gamma_rates) * bindec($epsilon_rates);
echo "\nAnswer: " . $answer;
}
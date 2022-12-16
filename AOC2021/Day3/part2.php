<?php
$input = file_get_contents("input.txt");
$handle = fopen("input.txt", "r");
if ($handle) {

    $data_array = [];
    while (($data = fgets($handle)) !== false) {
        $data = preg_replace("/\r|\n/", "", $data);
        $data_array[] = $data;
    }

fclose($handle);

    $total = count($data_array);
    $length = strlen($data_array[0]);


    $oxygen_generator_rating = findOxygenGeneratorRating(0, $data_array, $length);
    $co2_scrubber_rating = findCO2ScrubberRating(0, $data_array, $length);

    $life_support_rating = bindec($oxygen_generator_rating) * bindec($co2_scrubber_rating);

echo "\nAnswer: " . $life_support_rating;
}


function findOxygenGeneratorRating($position, $data, $length)
{
    /* echo "position: $position \n";
    print_r($data);
    echo "\n--------------------\n"; */
$total = count($data);
$zero_array = [];
$one_array = [];
for ($i = 0; $i < $total; $i++) {
    if (empty($data[$i][$position])) {
        $zero_array[] = $data[$i];
    } else {
        $one_array[] = $data[$i];
    }
}

if (count($data) == 1) {
    return $data[0];
} else if (count($data) == 2) {
    if ($data[0][$length - 1] == 1) {
        return $data[0];
    } else {
        return $data[1];
    }
} else {
    $position++;

    if (count($zero_array) == count($one_array)) {
        return findOxygenGeneratorRating($position, $one_array, $length);
    } else if (count($zero_array) > count($one_array)) {
        return findOxygenGeneratorRating($position, $zero_array, $length);
    } else {
        return findOxygenGeneratorRating($position, $one_array, $length);
    }
}
}


function findCO2ScrubberRating($position, $data, $length)
{
    $total = count($data);
    $zero_array = [];
    $one_array = [];
    for ($i = 0; $i < $total; $i++) {
        if (empty($data[$i][$position])) {
            $zero_array[] = $data[$i];
        } else {
            $one_array[] = $data[$i];
        }
}

if (count($data) == 1) {
    return $data[0];
} else if (count($data) == 2) {
    if ($data[0][$length - 1] == 0) {
        return $data[0];
    } else {
        return $data[1];
    }
} else {
    $position++;

    if (count($zero_array) == count($one_array)) {
        return findCO2ScrubberRating($position, $zero_array, $length);
    } else if (count($zero_array) < count($one_array)) {
        return findCO2ScrubberRating($position, $zero_array, $length);
    } else {
        return findCO2ScrubberRating($position, $one_array, $length);
    }
}
}
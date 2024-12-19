import { pins } from "@dsboard/pico_w"
import { sleep} from "@devicescript/core"
import "@devicescript/gpio"
import { startPotentiometer } from "@devicescript/servers"


const ADC0Server = startPotentiometer({pin: pins.GP26});

const joystickMin = 0;
const joystickMiddle = 0.5;
const joystickMax = 1;

const initialValue = await ADC0Server.reading.read();
const offset = initialValue - 0.5;
// const roundedOffset = Math.round(offset * 100) / 100;

ADC0Server.reading.subscribe(async (value) => {
    
    const invertedValue = (value - 1) * -1; // swap axis direction because we mount joystick in reverse position on controller
    let fixedRoundedValue = value;
    
    if (value > initialValue)   {
        const higherRange = joystickMax - initialValue;
        const percentageInHigherRange = (value-initialValue) * 100 / higherRange;
        const fixedValue = percentageInHigherRange * joystickMax / 100;
        fixedRoundedValue = Math.round(fixedValue * 100) / 100;
    }
    else {
        const lowerRange = initialValue;
        const perntageInLowerRange = value * 100 / lowerRange;
        const fixedValue = perntageInLowerRange * joystickMiddle / 100;
        fixedRoundedValue = Math.round(fixedValue * 100) / 100;
    }

    console.log("ADC0: " + fixedRoundedValue);
    await sleep(100);
 });

// function normalize(value: number): number {
//     return value / 3.3;
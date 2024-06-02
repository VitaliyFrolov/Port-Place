'use client'
import React, {useRef, useState, useEffect, FC} from "react";
import { useElementOnScreen } from "@/shared/hooks/useElementOnScreenю";

interface OpacityProps {
    children: any;
    delay?: any;
    className?: string;
};

export const Opacity: FC<OpacityProps> = ({children, delay, className}) => {
    const ref = useRef(null);
    const [ opacity, setOpacity ] = useState(0);
    const onScreen = useElementOnScreen(ref, "", 0.5);

    useEffect(() => {
        if(onScreen) {
            setOpacity(1);            
        }
        
    }, [onScreen])

    return (
        <div
            ref={ref}
            style={{
                opacity: opacity,
                transition: "0.7s ease-in-out",
                transitionDelay: delay ? delay : "none",
            }}
            className={className ? className : ""}
        >
            {children}
        </div>
    );
};
'use client'

import React, { useRef, useEffect } from 'react';
import styles from './Ticker.module.scss';

interface TickerProps {
    data: string;
};

export const Ticker: React.FC<TickerProps> = ({ data }) => {
    const tickerRef = useRef<HTMLDivElement>(null);
    const animationFrameRef = useRef<number>(0);

    const animate = () => {
        if (tickerRef.current) {
            const firstChild = tickerRef.current.firstChild as HTMLElement;
            const firstChildWidth = firstChild.offsetWidth;

            tickerRef.current.scrollLeft += 1;

            if (tickerRef.current.scrollLeft >= firstChildWidth) {
                tickerRef.current.scrollLeft = 0;
            }
        }
        animationFrameRef.current = requestAnimationFrame(animate);
    };

    useEffect(() => {
        animationFrameRef.current = requestAnimationFrame(animate);
        return () => cancelAnimationFrame(animationFrameRef.current);
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <section ref={tickerRef} className={styles.line__wrapper}>
            <span className={styles.line__list}>
                {data}
            </span>
            <span className={styles.line__list}>
                {data}
            </span>
        </section>
    );
};
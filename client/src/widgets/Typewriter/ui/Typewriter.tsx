import { FC } from 'react';
import styles from './Typewriter.module.scss';
import cn from 'classnames';

interface TypewriterProps {
    text: string;
    className?: string;
}

export const Typewriter: FC<TypewriterProps> = (props) => {
    const {
        text,
        className,
    } = props;

    return (
        <div className={cn([styles.text, className])}>
            {text}
        </div>
    )
};

//FIXME: Поправить каретку
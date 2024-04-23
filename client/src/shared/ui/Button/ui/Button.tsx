import { FC } from 'react';
import cn from 'classnames';
import styles from './Button.module.scss';

interface IButtonProps {
    className?: string;
    onClick?: () => void;
    children?: string;
}

export const Button: FC<IButtonProps> = (props) => {
    const {
        className,
        children,
        onClick,
    } = props;

    return (
       <button className={cn([styles.button, className])} onClick={onClick}>
            <span className={styles.caption}>
                {children}
            </span>
       </button>
    );
};